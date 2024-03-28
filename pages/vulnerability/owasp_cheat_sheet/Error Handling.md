エラーハンドリングチートシート¶

概要¶
エラーハンドリングはアプリケーション全体のセキュリティの一部です。映画の中ではなく、攻撃は常に偵察フェーズから始まります。このフェーズでは、攻撃者はアプリケーションサーバー、フレームワーク、ライブラリなど、ターゲットに関するできるだけ多くの技術情報（通常は名前やバージョンのプロパティなど）を収集しようとします。

未処理のエラーは、この最初のフェーズで攻撃者を支援し、攻撃の残りの部分にとって非常に重要です。

以下のリンクは、攻撃のさまざまなフェーズの説明を提供しています。

コンテキスト¶
エラーハンドリングレベルの問題は、ターゲットに関する多くの情報を明らかにすることができ、また、ターゲットの機能のインジェクションポイントを特定するためにも使用される可能性があります。

以下は、ユーザーに表示される例外を介してテクノロジースタック（ここではStruts2およびTomcatのバージョン）が開示される例です：

HTTPステータス500 - For input string: "null"

タイプの例外レポート

メッセージ 入力文字列のため: "null"

説明 サーバーはこのリクエストを完了できない内部エラーに遭遇しました。

例外

java.lang.NumberFormatException: 入力文字列のため: "null"
    java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)
    java.lang.Integer.parseInt(Integer.java:492)
    java.lang.Integer.parseInt(Integer.java:527)
    sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
    sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    java.lang.reflect.Method.invoke(Method.java:606)
    com.opensymphony.xwork2.DefaultActionInvocation.invokeAction(DefaultActionInvocation.java:450)
    com.opensymphony.xwork2.DefaultActionInvocation.invokeActionOnly(DefaultActionInvocation.java:289)
    com.opensymphony.xwork2.DefaultActionInvocation.invoke(DefaultActionInvocation.java:252)
    org.apache.struts2.interceptor.debugging.DebuggingInterceptor.intercept(DebuggingInterceptor.java:256)
    com.opensymphony.xwork2.DefaultActionInvocation.invoke(DefaultActionInvocation.java:246)
    ...

注: ルート原因の完全なスタックトレースは、Apache Tomcat/7.0.56ログで利用可能です。
以下は、インジェクションポイントを特定するために使用できる、サイトのインストールパスとともにSQLクエリエラーが開示される例です：

Warning: odbc_fetch_array() expects parameter /1 to be resource, boolean given
in D:\app\index_new.php on line 188
OWASPテストガイドは、アプリケーションから技術情報を取得するためのさまざまなテクニックを提供しています。

目的¶
この記事では、アプリケーションのランタイム設定の一部としてグローバルエラーハンドラーをどのように構成するかを示しています。場合によっては、このエラーハンドラーをコードの一部として定義する方が効率的な場合があります。その結果、予期しないエラーが発生した場合は、アプリケーションから汎用的な応答が返され、エラーの詳細がサーバーサイドにログ記録されて調査され、ユーザーに返されません。

次のスキーマは、対象アプローチを示しています：

概要

ほとんどの最近のアプリケーショントポロジーはAPIベースなので、この記事ではバックエンドがREST APIのみを公開し、ユーザーインターフェースのコンテンツを含まないと仮定しています。アプリケーションは、可能なすべての障害モードを徹底的にカバーし、5xxエラーを使用して、フルフィルできないリクエストへの応答を示すだけで、レスポンスの一部として実装の詳細を明らかにしません。そのため、RFC 7807 - HTTP APIのための問題の詳細は、ドキュメント形式を定義しています。
エラーロギング操作自体については、ロギングチートシートを使用する必要があります。この記事はエラーハンドリング部分に焦点を当てています。

提案¶
各テクノロジースタックについて、次の構成オプションが提案されています：

標準Java Webアプリケーション¶
この種のアプリケーションでは、web.xmlデプロイメント記述子レベルでグローバルエラーハンドラーを構成できます。

ここでは、Servlet仕様バージョン2.5以上から使用できる構成を提案します。

この構成では、予期しないエラーが発生すると、エラーがトレースされ、汎用的な応答が返されるように、

ページerror.jspへのリダイレクトが発生します。

web.xmlファイルへのリダイレクトの構成：

<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ns="http://java.sun.com/xml/ns/javaee"
xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
version="3.0">
...
    <error-page>
        <exception-type>java.lang.Exception</exception-type>
        <location>/error.jsp</location>
    </error-page>
...
</web-app>
error.jspファイルの内容：

<%@ page language="java" isErrorPage="true" contentType="application/json; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
String errorMessage = exception.getMessage();
//Log the exception via the content of the implicit variable named "exception"
//...
//We build a generic response with a JSON format because we are in a REST API app context
//We also add an HTTP response header to indicate to the client app that the response is an error
response.setHeader("X-ERROR", "true");
//Note that we're using an internal server error response
//In some cases it may be prudent to return 4xx error codes, when we have misbehaving clients
response.setStatus(500);
%>
{"message":"An error occur, please retry"}
Java SpringMVC/SpringBoot web application¶
SpringMVCまたはSpringBootを使用すると、プロジェクトで次のクラスを実装することでグローバルエラーハンドラーを定義できます。Spring Framework 6はRFC 7807に基づく問題の詳細を導入しました。

@ExceptionHandlerアノテーションを介して、アプリケーションによってjava.lang.Exceptionクラスを拡張する任意の例外がスローされたときにハンドラーが動作するようにハンドラーに指示します。また、ProblemDetailクラスを使用して応答オブジェクトを作成します。

import org.springframework.http.HttpStatus;
import org.springframework.http.ProblemDetail;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

/**
 * Global error handler in charge of returning a generic response in case of unexpected error situation.
 */
@RestControllerAdvice
public class RestResponseEntityExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler(value = {Exception.class})
    public ProblemDetail handleGlobalError(RuntimeException exception, WebRequest request) {
        //Log the exception via the content of the parameter named "exception"
        //...
        //Note that we're using an internal server error response
        //In some cases it may be prudent to return 4xx error codes, if we have misbehaving clients
        //By specification, the content-type can be "application/problem+json" or "application/problem+xml"
        return ProblemDetail.forStatusAndDetail(HttpStatus.INTERNAL_SERVER_ERROR, "An error occur, please retry");
    }
}
参考文献：

Springによる例外処理
SpringBootによる例外処理
ASP NET Core web application¶
ASP.NET Coreでは、例外ハンドラーが専用のAPIコントローラーであることを示すことで、グローバルエラーハンドラーを定義できます。

エラーハンドリングに専用のAPIコントローラーを使用するAPIコントローラーの内容：

using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Net;

namespace MyProject.Controllers
{
    /// <summary>
    /// API Controller used to intercept and handle all unexpected exception
    /// </summary>
    [Route("api/[controller]")]
    [ApiController]
    [AllowAnonymous]
    public class ErrorController : ControllerBase
    {
        /// <summary>
        /// Action that will be invoked for any call to this Controller in order to handle the current error
        /// </summary>
        /// <returns>A generic error formatted as JSON because we are in a REST API app context</returns>
        [HttpGet]
        [HttpPost]
        [HttpHead]
        [HttpDelete]
        [HttpPut]
        [HttpOptions]
        [HttpPatch]
        public JsonResult Handle()
        {
            //Get the exception that has implied the call to this controller
            Exception exception = HttpContext.Features.Get<IExceptionHandlerFeature>()?.Error;
            //Log the exception via the content of the variable named "exception" if it is not NULL
            //...
            //We build a generic response with a JSON format because we are in a REST API app context
            //We also add an HTTP response header to indicate to the client app that the response
            //is an error
            var responseBody = new Dictionary<String, String>{ {
                "message", "An error occur, please retry"
            } };
            JsonResult response = new JsonResult(responseBody);
            //Note that we're using an internal server error response
            //In some cases it may be prudent to return 4xx error codes, if we have misbehaving clients
            response.StatusCode = (int)HttpStatusCode.InternalServerError;
            Request.HttpContext.Response.Headers.Remove("X-ERROR");
            Request.HttpContext.Response.Headers.Add("X-ERROR", "true");
            return response;
        }
    }
}
アプリケーションStartup.csファイルで例外ハンドラーを専用のエラーハンドリングAPIコントローラーにマッピングする定義：

using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

namespace MyProject
{
    public class Startup
    {
...
        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            //First we configure the error handler middleware!
            //We enable the global error handler in others environments than DEV
            //because debug page are useful during implementation
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                //Our global handler is defined on "/api/error" URL so we indicate to the
                //exception handler to call this API controller
                //on any unexpected exception raised by the application
                app.UseExceptionHandler("/api/error");

                //To customize the response content type and text, use the overload of
                //UseStatusCodePages that takes a content type and format string.
                app.UseStatusCodePages("text/plain", "Status code page, status code: {0}");
            }

            //We configure others middlewares, remember that the declaration order is important...
            app

.UseMvc();
            //...
        }
    }
}
参考文献：

ASP.Net Coreによる例外処理
ASP NET Web API web application¶
ASP.NET Web API（.NET Coreフレームワークではなく標準.NETフレームワークから）を使用すると、アプリケーションで発生するエラーをトレースおよび処理するためにハンドラーを定義および登録できます。

エラーの詳細をトレースするためのハンドラーの定義：

using System;
using System.Web.Http.ExceptionHandling;

namespace MyProject.Security
{
    /// <summary>
    /// Global logger used to trace any error that occurs at application wide level
    /// </summary>
    public class GlobalErrorLogger : ExceptionLogger
    {
        /// <summary>
        /// Method in charge of the management of the error from a tracing point of view
        /// </summary>
        /// <param name="context">Context containing the error details</param>
        public override void Log(ExceptionLoggerContext context)
        {
            //Get the exception
            Exception exception = context.Exception;
            //Log the exception via the content of the variable named "exception" if it is not NULL
            //...
        }
    }
}
エラーを処理して汎用的な応答を返すためのハンドラーの定義：

using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Web.Http;
using System.Web.Http.ExceptionHandling;

namespace MyProject.Security
{
    /// <summary>
    /// Global handler used to handle any error that occurs at application wide level
    /// </summary>
    public class GlobalErrorHandler : ExceptionHandler
    {
        /// <summary>
        /// Method in charge of handle the generic response send in case of error
        /// </summary>
        /// <param name="context">Error context</param>
        public override void Handle(ExceptionHandlerContext context)
        {
            context.Result = new GenericResult();
        }

        /// <summary>
        /// Class used to represent the generic response send
        /// </summary>
        private class GenericResult : IHttpActionResult
        {
            /// <summary>
            /// Method in charge of creating the generic response
            /// </summary>
            /// <param name="cancellationToken">Object to cancel the task</param>
            /// <returns>A task in charge of sending the generic response</returns>
            public Task<HttpResponseMessage> ExecuteAsync(CancellationToken cancellationToken)
            {
                //We build a generic response with a JSON format because we are in a REST API app context
                //We also add an HTTP response header to indicate to the client app that the response
                //is an error
                var responseBody = new Dictionary<String, String>{ {
                    "message", "An error occur, please retry"
                } };
                // Note that we're using an internal server error response
                // In some cases it may be prudent to return 4xx error codes, if we have misbehaving clients 
                HttpResponseMessage response = new HttpResponseMessage(HttpStatusCode.InternalServerError);
                response.Headers.Add("X-ERROR", "true");
                response.Content = new StringContent(JsonConvert.SerializeObject(responseBody),
                                                     Encoding.UTF8, "application/json");
                return Task.FromResult(response);
            }
        }
    }
}
アプリケーションWebApiConfig.csファイルで両方のハンドラーを登録する：

using MyProject.Security;
using System.Web.Http;
using System.Web.Http.ExceptionHandling;

namespace MyProject
{
    public static class WebApiConfig
    {
        public static void Register(HttpConfiguration config)
        {
            //Register global error logging and handling handlers in first
            config.Services.Replace(typeof(IExceptionLogger), new GlobalErrorLogger());
            config.Services.Replace(typeof(IExceptionHandler), new GlobalErrorHandler());
            //Rest of the configuration
            //...
        }
    }
}
csharp <system.web>ノード内のWeb.configファイルでcustomErrorsセクションを以下のように設定します。

<configuration>
    ...
    <system.web>
        <customErrors mode="RemoteOnly"
                      defaultRedirect="~/ErrorPages/Oops.aspx" />
        ...
    </system.web>
</configuration>
参考文献：

ASP.Net Web APIによる例外処理

ASP.NETエラーハンドリング

プロトタイプのソース¶
適切なセットアップを見つけるために作成されたすべてのサンドボックスプロジェクトのソースコードは、このGitHubリポジトリに格納されています。

付録 HTTPエラー¶
HTTPエラーのリファレンスはこちらのRFC 2616にあります。実装の詳細を提供しないエラーメッセージを使用することは情報漏えいを避けるために重要です。一般に、HTTPクライアントのエラー（例：認証されていないアクセス、リクエストボディが大きすぎる）に起因するリクエストには4xxエラーコードを使用し、サーバーサイドでトリガされるエラーには5xxを使用します。予期しないバグ。アプリケーションが5xxエラーの監視を行うようにしてください。これは、一部の入力セットでアプリケーションが失敗する良い指標です。