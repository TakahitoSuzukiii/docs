概要¶
このページは、開発者向けの迅速な基本的な.NETセキュリティのヒントを提供することを目的としています。

.NET Framework¶
.NET Frameworkは、Microsoftの主要なエンタープライズ開発プラットフォームです。ASP.NET、Windowsデスクトップアプリケーション、Windows Communication Foundationサービス、SharePoint、Visual Studio Tools for Officeなどの技術のサポートAPIです。

.NET Frameworkは、高度な型システムの使用、データ、グラフィックス、ネットワーキング、ファイル操作などを管理するためのAPIのコレクションで構成されています。基本的に、Microsoftエコシステム内でのエンタープライズアプリケーションの開発に関するほとんどの要件をカバーしています。これは、ほぼ普遍的に使用されるライブラリであり、アセンブリレベルで強く名前付けされ、バージョン管理されています。

フレームワークの更新¶
.NET Frameworkは、Windows UpdateサービスによってMicrosoftによって常に最新の状態に保たれています。通常、開発者はフレームワークを別個に更新する必要はありません。Windows Updateは、Windowsコンピューター上のWindows UpdateまたはWindows Updateプログラムからアクセスできます。

個々のフレームワークは、NuGetを使用して最新の状態に保つことができます。Visual Studioが更新を促す場合は、ライフサイクルに組み込んでください。

サードパーティのライブラリは別個に更新する必要があり、すべてがNuGetを使用しているわけではありません。たとえば、ELMAHは別個の更新作業が必要です。

セキュリティのお知らせ¶
以下のリポジトリで "Watch"ボタンを選択してセキュリティ通知を受け取ります。

.NET Coreセキュリティのお知らせ
ASP.NET Core＆Entity Framework Coreセキュリティのお知らせ
.NETの一般的なガイダンス¶
このセクションには、.NETアプリケーションの一般的なガイダンスが含まれています。これは、ASP.NET、WPF、WinFormsなど、すべての.NETアプリケーションに適用されます。

OWASP Top 10は、今日のウェブセキュリティに対する最も普及しており、危険な脅威をリストアップしています。このチートシートのこのセクションは、このリストに基づいています。ウェブアプリケーションのセキュリティを確保するアプローチは、以下の最上位の脅威A1から開始し、それ以降のセキュリティに費やす時間が最も効果的に使われ、最初に上位の脅威がカバーされるようにすることです。トップ10をカバーした後は、通常、他の脅威を評価したり、専門家によって完了されたペネトレーションテストを受けることが望ましいです。

A01 アクセス制御の破損¶
弱いアカウント管理¶
クライアント側のスクリプトからクッキーにアクセスできないように、HttpOnlyフラグが設定されていることを確認してください。

CookieHttpOnly = true,
セッションが盗まれる可能性を減らすために、セッションのタイムアウトを短縮し、スライディング有効期限を削除します。

ExpireTimeSpan = TimeSpan.FromMinutes(60),
SlidingExpiration = false
ここを参照して、完全な起動時のコードスニペットの例をご覧ください。

本番環境でクッキーがHTTPS経由で送信されるようにする必要があります。これは、構成の変換で強制する必要があります。

<httpCookies requireSSL="true" />
<authentication>
    <forms requireSSL="true" />
</authentication>
LogOn、Registration、およびパスワードリセットメソッドを、スロットルリクエストによってブルートフォース攻撃から保護します（以下のコードを参照）。ReCaptchaの使用も検討してください。
[HttpPost]
[AllowAnonymous]
[ValidateAntiForgeryToken]
[AllowXRequestsEveryXSecondsAttribute(Name = "LogOn",
Message = "過去{n}秒間に{X}回を超えるこのアクションを実行しました。",
Requests = 3, Seconds = 60)]
public async Task<ActionResult> LogOn(LogOnViewModel model, string returnUrl)
行わないでください：独自の認証またはセッション管理を行わないでください。.NETで提供されるものを使用してください。

行わないでください：ログオン、登録、またはパスワードリセット時にアカウントが存在するかどうかを誰かに伝えないでください。 'ユーザー名またはパスワードが間違っています'などと言うか、 'このアカウントが存在する場合は、登録されたメールアドレスにリセットトークンが送信されます'と言うかを考えてください。これにより、アカウントの列挙に対して保護されます。

アカウントが存在するかどうかにかかわらず、ユーザーへのフィードバックは、コンテンツと動作の両方について同一である必要があります。たとえば、アカウントが実際に存在する場合、応答に時間が50％かかる場合は、メンバーシップ情報が推測およびテストされる可能性があります。

機能レベルのアクセス制御の不足¶
すべての外部に面したエンドポイントでユーザーを認可してください。 .NETフレームワークには、ユーザーを認可するためのさまざまな方法があります。メソッドレベルでそれらを使用してください。

[Authorize(Roles = "Admin")]
[HttpGet]
public ActionResult Index(int page = 1)
または、より良い方法として、コントローラーレベルで：

[Authorize]
public class UserController
.identity features in .netを使用してコードで役割を確認することもできます：System.Web.Security.Roles.IsUserInRole(userName, roleName)

Authorization Cheat SheetとAuthorization Testing Automation Cheat Sheetで詳細をご覧いただけます。

安全でない直接オブジェクト参照¶
（以下のサンプルでは、idがそれに該当する）

リソース（オブジェクト）にアクセスできるリファレンスがある場合、ユーザーがそのリソースにアクセスすることが意図されていることを確認する必要があります。

// 安全でない
public ActionResult Edit(int id)
{
var user = _context.Users.FirstOrDefault(e => e.Id == id);
return View("Details", new UserViewModel(user);
}

// 安全
public ActionResult Edit(int id)
{
var user = _context.Users.FirstOrDefault(e => e.Id == id);
// ユーザーが詳細を編集する権限があることを確立する
if (user.Id != _userIdentity.GetUserId())
{
HandleErrorInfo error = new HandleErrorInfo(
new Exception("INFO: これらの詳細を編集する権限がありません"));
return View("Error", error);
}
return View("Edit", new UserViewModel(user);
}
安全な直接オブジェクト参照防止チートシートで詳細を確認できます。

A02 暗号化の失敗¶
一般的な暗号化のガイダンス¶
決して、決して独自の暗号化関数を作成しないでください。
可能な限り、暗号化コードを書かないようにしてください。代わりに、既存の秘密管理ソリューションまたはクラウドプロバイダーが提供する秘密管理ソリューションを使用しようとしてください。詳細については、OWASP Secrets Management Cheat Sheetを参照してください。
既存の秘密管理ソリューションを使用できない場合は、.NETに組み込まれているライブラリを使用する代わりに、信頼できる既知の実装ライブラリを使用してください。.NETは、これらのライブラリを使用すると暗号化エラーが非常に発生しやすくなります。
アプリケーションまたはプロトコルが将来の暗号化アルゴリズムの変更を容易にサポートできることを確認してください。
ハッシュ化¶
強力なハッシュ化アルゴリズムを使用してください。

.NET（FrameworkおよびCoreの両方）では、一般的なハッシュ化要件に最適な最強のハッシュ化アルゴリズムは、System.Security.Cryptography.SHA512です。
.NET Framework 4.6以前では、パスワードのハッシュ化に最強のアルゴリズムは、System.Security.Cryptography.Rfc2898DeriveBytesとして実装されたPBKDF2です。
.NET Framework 4.6.1以降および.NET Coreでは、パスワードのハッシュ化に最強のアルゴリズムは、Microsoft.AspNetCore.Cryptography.KeyDerivation.Pbkdf2として実装されたPBKDF2です。これには、Rfc2898DeriveBytesよりも大幅に優れた利点があります。
パスワードなどの一意でない入力をハッシュ化関数でハッシュ化する場合は、ハッシュ化する前に元の値に追加するソルト値を使用してください。
詳細については、Password Storage Cheat Sheetを参照してください。
パスワード¶
辞書攻撃を生き延びる最小の複雑さを持つパスワードを強制してください。つまり、エントロピーを増やすために完全な文字セット（数字、記号、文字）を使用した長いパスワードを使用してください。

暗号化¶
個人を特定できるデータを元の形式に復元する場合は、AES-512などの強力な暗号化アルゴリズムを使用してください。

他の資産よりも暗号化キーを保護してください。静止状態での暗号化キーの格納に関する詳細は、Key Management Cheat Sheetを参照してください。

サイト全体でTLS 1.2+を使用してください。無料の証明書LetsEncrypt.orgを取得して更新を自動化してください。

SSLを許可しないでください。これは今や時代遅れです。

強力なTLSポリシーを持ってください（SSLベストプラクティスを参照）、できる限りTLS 1.2+を使用してください。その後、SSLテストまたはTestSSLを使用して構成を確認してください。

トランスポートレイヤー保護の詳細については、Transport Layer Security Cheat Sheetを参照してください。

ヘッダーがアプリケーションに関する情報を開示していないことを確認してください。HttpHeaders.cs、Dionach StripHeaders、web.config、またはStartup.csを使用して無効にします。

例：Web.config

<system.web>
<httpRuntime enableVersionHeader="false"/>
</system.web>
<system.webServer>
<security>
<requestFiltering removeServerHeader="true" />
</security>
<httpProtocol>
<customHeaders>
<add name="X-Content-Type-Options" value="nosniff" />
<add name="X-Frame-Options" value="DENY" />
<add name="X-Permitted-Cross-Domain-Policies" value="master-only"/>
<add name="X-XSS-Protection" value="0"/>
<remove name="X-Powered-By"/>
</customHeaders>
</httpProtocol>
</system.webServer>
例：Startup.cs

app.UseHsts(hsts => hsts.MaxAge(365).IncludeSubdomains());
app.UseXContentTypeOptions();
app.UseReferrerPolicy(opts => opts.NoReferrer());
app.UseXXssProtection(options => options.FilterDisabled());
app.UseXfo(options => options.Deny());

app.UseCsp(opts => opts
.BlockAllMixedContent()
.StyleSources(s => s.Self())
.StyleSources(s => s.UnsafeInline())
.FontSources(s => s.Self())
.FormActions(s => s.Self())
.FrameAncestors(s => s.Self())
.ImageSources(s => s.Self())
.ScriptSources(s => s.Self())
);
ヘッダーに関する詳細については、OWASP Secure Headers Projectを参照してください。

保存のための暗号化¶
機密データの安全なローカルストレージにWindows Data Protection API（DPAPI）を使用してください。
DPAPIを使用できない場合は、OWASP Cryptographic Storage Cheat Sheetのアルゴリズムガイダンスに従ってください。
次のコードスニペットは、データの暗号化/復号化を実行するためのAES-GCMの使用例を示しています。最終設計およびコードを暗号化の専門家に確認することを強くお勧めします。最も些細なエラーでも、暗号化が深刻に弱体化する可能性があります。

このコードは、こちらの例に基づいています：https://www.scottbrady91.com/c-sharp/aes-gcm-dotnet

このコードにはいくつかの制約/落とし穴があります：

これは、鍵の回転や管理を考慮していませんが、これ自体が独立したトピックです。
同じキーを使用しても、暗号化操作ごとに異なるノンスを使用することが重要です。
鍵は安全に保存する必要があります。
ここをクリックして "AES-GCM対称暗号化"コードスニペットを表示します。
送信用の暗号化¶
再度、OWASP Cryptographic Storage Cheat Sheetのアルゴリズムガイダンスに従ってください。
次のコードスニペットは、Eliptic Curve/Diffie Helman（ECDH）を使用してAES-GCMと組み合わせて、二つの異なる側の間でデータの暗号化/復号化を実行する例を示しています。これにより、二つの側の間で対称キーを転送する必要がなくなります。代わりに、両側が公開鍵を交換し、ECDHを使用して共有シークレットを生成し、これを対称暗号化に使用できます。

再度、最終設計およびコードを暗号化の専門家に確認することを強くお勧めします。最も些細なエラーでも、暗号化が深刻に弱体化する可能性があります。

このコードサンプルでは、以前のセクションのAesGcmSimpleクラスに依存しています。

このコードにはいくつかの制約/落とし穴があります：

これは、鍵の回転や管理を考慮していませんが、これ自体が独立したトピックです。
コードは、すべての暗号化操作ごとに新しいノンスを強制するように意図的に設定されていますが、これは別個のデータ項目として処理する必要があります。
プライベートキーは安全に保存する必要があります。
コードは、使用前に公開鍵の検証を考慮していません。
全体的に、二つの側の間での真正性の検証はありません。
ここをクリックして "AES-GCM対称暗号化"コードスニペットを表示します。

インターネット接続経由での送信¶
メンテナンスを行う必要がある場合は、単純なHTTPセッションではなく、WebSocketを使用してください。

WebSocketは、セキュリティの更新を持っています。その機能は、常に使用されているTLS証明書によって制御されます。

HTTPSまたはWSSが可能な場合は、常にハードコードされたURLを使用してください。

IPアドレスは絶対に許可しません。これにより、TLSホスト名検証の問題が回避されます。

TLS経由のクライアント証明書ベースの認証が可能な場合は、クライアント認証を構成してください。これにより、APIを特定のクライアントに制限できます。

APIのトラフィックには、非常に安全なTLSセキュリティプロトコルが含まれていることを確認してください（TLS 1.2以降が推奨されます）。

暗号スイート（RC4など）を避け、セキュアな鍵交換アルゴリズム（ECDHなど）を使用してください。

TLSハードコーディングには、証明書の検証やその他の重要な要因を無視しないでください。

以下のリンクを使用して、安全な暗号スイートとサーバー設定の一般的なセキュリティを確認してください：

強化されたHTTPSハードニングとIIS SSLベストプラクティスを使用して、IISとNginxの最適な暗号スイートと設定を設定します。

SSL証明書¶
無料の証明書を使用してサービスにSSLを追加し、HTTPS接続を許可します（特に今日はLet's Encryptなどのサービスがあります）。

SSL証明書は定期的に更新してください。自動更新をセットアップすることを強くお勧めします。

SSL Labsを使用してSSL設定の評価と最適化を実行してください。

SSL証明書のプライベートキーを適切に保護し、暗号化されたままにしておくことを確認してください。

SSL証明書のチェーンは、信頼されたCAから発行されていることを確認してください。

HTTP Strict Transport Security（HSTS）¶
サーバーレスポンスヘッダーにHSTSを含め、ブラウザにHTTPSへの強制的なリダイレクトを宣言します。

すべてのサブドメインを含めるか、必要に応じて、設定します（includeSubDomainsディレクティブ）。

HSTSの期間を1年以上に設定してください。これにより、HTTPS接続が強制されるようになります。

詳細については、OWASP HTTP Strict Transport Security Cheat Sheetを参照してください。

暗号化の完了¶
データの暗号化が完了すると、それ以上変更できないことを確認してください。また、データの完全性も確認してください。データが変更された場合、それを検出して適切なアクションを実行できるようにします。

完全性の検証が機能していることを確認するために、鍵またはデータのエイリアスを使用してハッシュを計算することを強くお勧めします。

.NETアプリケーションで完全性の保護を実装するために、SHA-256やSHA-3のような強力なハッシュ関数を使用して、データの整合性を検証します。

詳細については、OWASP Cryptographic Storage Cheat Sheetを参照してください。

認証¶
アプリケーション間通信¶
アプリケーション間の通信には常に認証が必要です。認証を行わずに通信を許可しないでください。

次のセクションには、認証の例が示されています。

APIトークン¶
セキュリティトークンの発行には、OAuth 2.0やOpenID Connectなどの標準的なプロトコルを使用してください。独自のトークン機構を作成しないでください。

アクセストークンを保存する場所を慎重に選択してください。通常、セキュリティで保護されたCookieまたはBearerトークンとしてメモリ内に保存されます。

トークンの有効期限を制限してください。長時間の有効期間はセキュリティリスクです。

トークンを適切にリフレッシュし、古いトークンを再利用しないでください。

OAuth 2.0やOpenID Connectなどのプロトコルを使用する場合は、サードパーティのライブラリを使用してください。自前で実装しないでください。

トークンを発行する際には、安全なランダム文字列ジェネレーターを使用してください。

詳細については、OWASP API Security Cheat SheetとOAuth 2.0 Threat Model and Security Considerationsを参照してください。

CORS¶
Cross-Origin Resource Sharing（CORS）を実装して、安全にアプリケーション間の通信を行います。これにより、意図しないクロスサイトリクエストが許可されるのを防ぎます。

適切な設定を使用して、信頼されたオリジンのみがリソースにアクセスできるようにします。

必要に応じて、アクセス許可されたリソースに対するリクエストの処理を制限します。

CORSの構成に関する詳細については、MDN Web DocsのCORSを参照してください。

ファイルのアップロード¶
ファイルアップロードのサイズと種類を制限してください。これにより、悪意のあるユーザーが脆弱性を利用して大量のファイルをアップロードしてサーバーをオーバーロードすることが防止されます。

アップロードされたファイルのコンテンツを検証し、許可されたファイルタイプおよび形式であることを確認してください。ファイルタイプが不明な場合は、拡張子に頼らずに内容を解析することを検討してください。

ファイルの名前に対する検証が重要です。悪意のあるユーザーが脆弱性を悪用して、システムのディレクトリ構造に不適切なファイル名を挿入することが防止されます。

ファイルのアップロードを受け入れる前に、サーバー側で設定された一時フォルダに保存するなど、安全な方法でアップロードされたファイルを処理してください。

システム上でアップロードされたファイルに関連するセキュリティ上のリスクを理解し、セキュリティ対策を実施してください。これには、ファイルのスキャン、不要なファイルの削除、データの暗号化、必要な場合のデータのマスキングなどが含まれます。

アップロードされたファイルに関連する機密情報を含めないでください。ファイルに機密情報が含まれている場合は、その情報を取り除くか、ファイル全体を暗号化してください。

安全なアップロードの実装に関する詳細については、OWASP Secure File Upload Cheat Sheetを参照してください。

ファイルのダウンロード¶
安全なファイルダウンロードを実装するために、ユーザーがダウンロードできるファイルに関連するセキュリティ上のリスクを理解し、適切なセキュリティ対策を実施してください。

ファイルのダウンロードが許可されているユーザーに制限を設け、アクセス権を与えられていないユーザーがファイルをダウンロードできないようにしてください。

ファイルのダウンロードを提供する前に、ダウンロードされるファイルがセキュリティで保護され、信頼できるソースから提供されていることを確認してください。

ファイルのダウンロードには、適切な認証と承認が必要です。ユーザーがダウンロードできるファイルは、そのユーザーに許可されたリソースにのみアクセスできるように制限されている必要があります。

ファイルのダウンロードのセキュリティ対策には、ファイルの検証、ファイルの暗号化、マルウェアスキャン、ファイルの不正操作の検出などが含まれます。

ファイルダウンロードに関連する機密情報を含めないでください。ファイルに機密情報が含まれている場合は、その情報を取り除くか、ファイル全体を暗号化してください。

詳細については、OWASP Secure File Download Cheat Sheetを参照してください。

データベース¶
データベースに安全なクエリを送信するための正しい方法を使用してください。SQLインジェクションを防ぐために、パラメータ化されたクエリやORMを使用してください。

データベースアクセスの認証と承認を適切に制御してください。アプリケーションは、必要な権限を持つユーザーのみがデータベースにアクセスできるようにする必要があります。

データベースに保存されるデータは、適切にエンコード、サニタイズ、およびバリデーションされている必要があります。これにより、悪意のあるデータがデータベースに挿入されることが防止されます。

データベースに保存される機密情報は、適切に暗号化されている必要があります。これにより、データが漏洩した場合でも保護されます。

データベースの接続情報は、適切に保護され、暗号化されている必要があります。これにより、悪意のあるユーザーがデータベースにアクセスすることが防止されます。

データベースの監査ログを適切に設定し、アクセス、変更、および他の重要なイベントを追跡および監視します。これにより、不正なアクティビティが早期に検出され、対処されます。

詳細については、OWASP SQL Injection Prevention Cheat SheetとOWASP Database Security Cheat Sheetを参照してください。

データベースのバックアップ¶
定期的かつ頻繁にデータベースのバックアップを作成してください。これにより、データが失われた場合でも、重要な情報を復元できます。

データベースのバックアップは、安全な場所に保存される必要があります。データベースバックアップは、データが失われた場合に備えて保護された場所に保存されている必要があります。

データベースのバックアップは、適切に暗号化される必要があります。これにより、機密情報が第三者によってアクセスされるのを防ぎます。

データベースのバックアップのテストを定期的に実施してください。これにより、バックアップが正しく機能し、データが必要なときに正常に復元できることが確認されます。

データベースのバックアップにアクセスするためのアクセス制御を適切に構成してください。バックアップは、必要なユーザーだけがアクセスできるように制限される必要があります。

バックアップデータは、適切に保護され、不正なアクセスから保護される必要があります。これにより、機密情報が不正な手に渡るのを防ぎます。

詳細については、OWASP Backup Security Cheat Sheetを参照してください。

セッション管理¶
セッション管理には、安全なセッションIDの生成、適切なセッションの有効期限の設定、セッション固定攻撃の防止、セッションの暗号化など、多くのセキュリティ上の考慮事項があります。

セッションIDは、予測可能なものではなく、十分なエントロピーを持つランダムな値である必要があります。これにより、セッションIDを推測してアクセスすることが困難になります。

セッションの有効期限は、セキュリティ要件に応じて適切に設定される必要があります。セッションがアクティブである間だけ有効であり、期限切れのセッションが自動的に破棄されるようにする必要があります。

セッション固定攻撃を防ぐために、セッションIDは認証される前に変更される必要があります。これにより、攻撃者が既存の有効なセッションIDをキャプチャして使用することを防ぎます。

セッションデータは、暗号化される必要があります。これにより、セッションデータがユーザーのプライバシーとセキュリティに影響を与える可能性がある場合でも、悪意のあるユーザーから保護されます。

セッション管理に関する詳細については、OWASP Session Management Cheat Sheetを参照してください。

パスワード管理¶
パスワードの長さ、複雑さ、および更新ポリシーを適切に設定してください。これにより、弱いパスワードが使用される可能性が減ります。

パスワードは、ハッシュ関数を使用して保存する前に適切に暗号化される必要があります。これにより、パスワードがデータベース内で平文のまま保存されるのを防ぎます。

パスワードのリセットと再発行には、適切な手順とセキュリティ検証が必要です。これにより、認証を回避してアクセスできる可能性がある悪意のあるユーザーが防止されます。

パスワードの複雑さと長さに関する要件は、ユーザーに適切に伝えられる必要があります。これにより、ユーザーがセキュリティポリシーに準拠したパスワードを選択できるようになります。

パスワードを安全に保存および管理するためのベストプラクティスに関する詳細については、OWASP Password Storage Cheat Sheetを参照してください。

認証の例¶
JWT（JSON Web Tokens）を使用したWebトークンの発行および認証

TLSに基づくクライアント証明書認証の構成

OAuth 2.0を使用したアクセストークンの発行と認証

Active DirectoryとLDAPを使用したシングルサインオン（SSO）

OAuth 2.0とOpenID Connectを使用したWebサイトの認証

認証の実装に関する詳細については、OWASP Authentication Cheat Sheetを参照してください。

これらのセキュリティ上のベストプラクティスは、アプリケーションのセキュリティを強化し、ユーザーのデータを保護するための基本的なガイドラインを提供します。しかし、セキュリティは常に変化し、新しい脅威や攻撃手法に対応するために最新のベストプラクティスを適用することが重要です。

A04 セキュリティデザインの脆弱性¶
セキュリティデザインの脆弱性とは、アプリケーションやシステムの設計上のセキュリティの失敗を指します。これは、OWASP Top 10リストの他の項目とは異なり、実装上の失敗を指します。したがって、セキュアなデザインのトピックは、特定の技術や言語に関連するものではなく、このチートシートの範囲外です。詳細については、セキュアプロダクトデザインチートシートを参照してください。

A05 セキュリティの誤構成¶
デバッグとスタックトレース¶
本番環境ではデバッグとトレースがオフになっていることを確認してください。これは、web.configの変換を使用して強制できます:

<compilation xdt:Transform="RemoveAttributes(debug)" />
<trace enabled="false" xdt:Transform="Replace"/>
デフォルトのパスワードを使用しないでください
HTTP経由でのリクエストをHTTPSにリダイレクトします:

例: Global.asax.cs:

protected void Application_BeginRequest()
{
#if !DEBUG
// SECURE: 本番環境でSSL/TLS経由でリクエストが返されることを確認します
if (!Request.IsLocal && !Context.Request.IsSecureConnection) {
var redirect = Context.Request.Url.ToString()
.ToLower(CultureInfo.CurrentCulture)
.Replace("http:", "https:");
Response.Redirect(redirect);
}
#endif
}
例: Startup.csのConfigure（）:

app.UseHttpsRedirection();
クロスサイトリクエストフォージェリ¶
アンチフォージェリトークン（.NET / .NET Core）を検証せずに、機密データを送信しないでください。

POST/PUTリクエストごとにアンチフォージェリトークンを送信してください:

.NET Frameworkを使用して¶
(Html.BeginFormを使用)

using (Html.BeginForm("LogOff", "Account", FormMethod.Post, new { id = "logoutForm",
@class = "pull-right" }))
{
@Html.AntiForgeryToken()
<ul class="nav nav-pills">
<li role="presentation">
ログイン中: @User.Identity.Name
</li>
<li role="presentation">
<a href="javascript:document.getElementById('logoutForm').submit()">ログオフ</a>
</li>
</ul>
}
次に、メソッドレベルまたは可能であればコントローラレベルでそれを検証してください:

[HttpPost]
[ValidateAntiForgeryToken]
public ActionResult LogOff()
無効化時にトークンが完全に削除されるようにしてください。

/// <summary>
/// SECURE: Anti-CSRFクッキーを含む残りのクッキーをすべて削除します
/// </summary>
public void RemoveAntiForgeryCookie(Controller controller)
{
string[] allCookies = controller.Request.Cookies.AllKeys;
foreach (string cookie in allCookies)
{
if (controller.Response.Cookies[cookie] != null &&
cookie == "__RequestVerificationToken")
{
controller.Response.Cookies[cookie].Expires = DateTime.Now.AddDays(-1);
}
}
}
.NET Core 2.0以降を使用して¶
.NET Core 2.0からは、アンチフォージェリトークンを自動生成および検証することが可能になりました。

デフォルトでほとんどのWebプロジェクトテンプレートで使用されるtag-helpersを使用している場合、すべてのフォームが自動的にアンチフォージェリトークンを送信します。tag-helpersが有効になっているかどうかは、主要な_ViewImports.cshtmlファイルが次の内容を含んでいるかどうかを確認することで確認できます:

@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
IHtmlHelper.BeginFormも自動的にアンチフォージェリトークンを送信します。

tag-helpersまたはIHtmlHelper.BeginFormを使用していない場合は、次のようにフォームに必要なヘルパーを使用する必要があります:

<form action="RelevantAction" >
@Html.AntiForgeryToken()
</form>
GET、HEAD、OPTIONS、TRACE以外のすべてのリクエストを自動的に検証するには、Startup.csにAutoValidateAntiforgeryToken属性を持つグローバルアクションフィルタを追加する必要があります。次の記事で説明されているように：
services.AddMvc(options =>
{
options.Filters.Add(new AutoValidateAntiforgeryTokenAttribute());
});
特定のコントローラのメソッドで属性の検証を無効にする必要がある場合は、IgnoreAntiforgeryToken属性をコントローラメソッド（MVCコントローラーの場合）または親クラス（Razorページの場合）に追加できます:

[IgnoreAntiforgeryToken]
[HttpDelete]
public IActionResult Delete()
[IgnoreAntiforgeryToken]
public class UnsafeModel : PageModel
GET、HEAD、OPTIONS、TRACEリクエストに対してトークンを検証する必要がある場合は、次のようにコントローラメソッド（MVCコントローラーの場合）または親クラス（Razorページの場合）にValidateAntiforgeryToken属性を追加します:

[HttpGet]
[ValidateAntiforgeryToken]
public IActionResult DoSomethingDangerous()
[HttpGet]
[ValidateAntiforgeryToken]
public class SafeModel : PageModel
グローバルアクションフィルタを使用できない場合は、AutoValidateAntiforgeryToken属性をコントローラクラスまたはRazorページモデルに追加してください:

[AutoValidateAntiforgeryToken]
public class UserController
[AutoValidateAntiforgeryToken]
public class SafeModel : PageModel
AJAXを使用した.NET Coreまたは.NET Framework¶
AJAXリクエストにアンチフォージェリトークンを添付する必要があります。

ASP.NET Core MVCビューでjQueryを使用している場合、次のスニペットを使用してこれを実現できます:

@inject Microsoft.AspNetCore.Antiforgery.IAntiforgery antiforgeryProvider
$.ajax(
{
type: "POST",
url: '@Url.Action("Action", "Controller")',
contentType: "application/x-www-form-urlencoded; charset=utf-8",
data: {
id: id,
'__RequestVerificationToken': '@antiforgeryProvider.GetAndStoreTokens(this.Context).RequestToken'
}
})
.NET Frameworkを使用している場合は、ここでいくつかのコードスニペットを見つけることができます。

詳細については、Cross-Site Request Forgery Prevention Cheat Sheetを参照してください。

A06 脆弱なおよび更新されていないコンポーネント¶
.NETフレームワークを最新のパッチで更新してください

NuGetパッケージを最新の状態に保つ

ビルドプロセスの一部としてアプリケーションにOWASP依存チェッカーを実行し、高いまたは重大なレベルの脆弱性に対処してください。

CI/CDパイプラインにSCA（ソフトウェア構成解析）ツールを含めて、依存関係の新しい脆弱性が検出および対処されるようにしてください。

A07 識別と認証の失敗¶
ASP.NET Core Identityを使用してください。ASP.NET Core Identityフレームワークはデフォルトで適切に構成されており、セキュアなパスワードハッシュと個々のソルトを使用しています。IdentityはパスワードのためにPBKDF2ハッシュ関数を使用し、ユーザごとにランダムなソルトを生成します。

セキュアなパスワードポリシーを設定してください

例：ASP.NET Core Identity

//Startup.cs
services.Configure<IdentityOptions>(options =>
{
// パスワード設定
options.Password.RequireDigit = true;
options.Password.RequiredLength = 8;
options.Password.RequireNonAlphanumeric = true;
options.Password.RequireUppercase = true;
options.Password.RequireLowercase = true;
options.Password.RequiredUniqueChars = 6;

options.Lockout.DefaultLockoutTimeSpan = TimeSpan.FromMinutes(30);
options.Lockout.MaxFailedAccessAttempts = 3;

options.SignIn.RequireConfirmedEmail = true;

options.User.RequireUniqueEmail = true;
});
クッキーポリシーを設定してください

例：

//Startup.cs
services.ConfigureApplicationCookie(options =>
{
options.Cookie.HttpOnly = true;
options.Cookie.Expiration = TimeSpan.FromHours(1)
options.SlidingExpiration = true;
});
A08 ソフトウェアおよびデータの整合性の失敗¶
アセンブリおよび実行可能ファイルにデジタル署名を付ける

Nugetパッケージ署名を使用する

悪意のあるコードや依存関係が導入されないように、コードと設定の変更を確認する

未署名または暗号化されていない直列化されたオブジェクトをネットワーク経由で送信しない

ネットワークから受信した直列化されたオブジェクトの整合性をチェックするか、デジタル署名を検証する

データ処理に推奨されていない危険なBinaryFormatterタイプを使用しない。.NETには、信頼できないデータを安全に処理できるいくつかのボックス内シリアライザが用意されています:

XMLとJSON用のXmlSerializerとDataContractSerializer
XMLとJSON用のBinaryReaderとBinaryWriter
オブジェクトグラフをJSONにシリアル化するためのSystem.Text.Json API
A09 セキュリティログおよび監視の失敗¶
すべてのログイン、アクセス制御、およびサーバー側の入力検証の失敗が、十分なユーザーコンテキストと共にログに記録されていることを確認してください。

怪しい活動がタイムリーに検出および対応されるように、効果的なモニタリングおよびアラート設定を確立してください。

csharp Log.Error("Error was thrown");などの汎用的なエラーメッセージをログに記録しないでください。代わりに、スタックトレース、エラーメッセージ、およびエラーの原因となったユーザーIDをログに記録してください。

ユーザーのパスワードなどの機密データをログに記録しないでください。

ログ¶
どのログを収集するかや、ログに関する詳細な情報は、ログのチートシートにあります。

.NET Coreには、Microsoft.Extensions.LoggingのLoggerFactoryが付属しています。ILoggerの詳細については、こちらを参照してください。

すべてのエラーをStartup.csからログに記録する方法:

public void Configure(IApplicationBuilder app, IHostingEnvironment env)
{
if (env.IsDevelopment())
{
_isDevelopment = true;
app.UseDeveloperExceptionPage();
}

javascript
Copy code
//アプリケーションで発生したすべてのエラーをログに記録
app.UseExceptionHandler(errorApp =>
{
    errorApp.Run(async context =>
    {
        var errorFeature = context.Features.Get<IExceptionHandlerFeature>();
        var exception = errorFeature.Error;

        Log.Error(String.Format("Stacktrace of error: {0}",exception.StackTrace.ToString()));
    });
});

app.UseAuthentication();
app.UseMvc();
}
}
例：クラスのコンストラクタにインジェクションすると、ユニットテストの作成が簡単になります。クラスのインスタンスが依存関係の注入を使用して作成される場合は、これを推奨します（たとえば、MVCコントローラ）。次の例は、すべての失敗したログイン試行をログに記録する方法を示しています。

public class AccountsController : Controller
{
private ILogger _Logger;

csharp
Copy code
    public AccountsController(ILogger logger)
    {
        _Logger = logger;
    }

    [HttpPost]
    [AllowAnonymous]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Login(LoginViewModel model)
    {
        if (ModelState.IsValid)
        {
            var result = await _signInManager.PasswordSignInAsync(model.Email, model.Password, model.RememberMe, lockoutOnFailure: false);
            if (result.Succeeded)
            {
                //すべての成功したログイン試行をログに記録
                Log.Information(String.Format("User: {0}, Successfully Logged in", model.Email));
                //成功したログインのためのコード
                //...
            }
            else
            {
                //すべての不正なログイン試行をログに記録
                Log.Information(String.Format("User: {0}, Incorrect Password", model.Email));
            }
         }
        ...
    }
監視¶
監視を行うことで、実行中のシステムのパフォーマンスと健全性をキーのパフォーマンス指標を通じて検証できます。

.NETで監視機能を追加する素晴らしい方法は、Application Insightsです。

ログと監視に関する詳細はこちらで見つけることができます。

A10 サーバーサイドのリクエスト偽造（SSRF）¶
リクエストを行う前に、すべてのユーザー入力を検証して消毒してください

許可されたプロトコルとドメインの許可リストを使用してください

IPアドレスとドメイン名が有効であることを確認するために、IPAddress.TryParse（）およびUri.CheckHostName（）を使用してください

HTTPリダイレクトをフォローしないでください

生のHTTP応答をユーザーに転送しないでください

詳細については、Server-Side Request Forgery Prevention Cheat Sheetをご覧ください。

OWASP 2013＆2017¶
2013年または2017年のOWASP Top 10リストに含まれていた脆弱性で、2021年のリストには含まれていなかったものが以下に示されています。これらの脆弱性は依然として関連性がありますが、2021年のリストに含まれていませんでした。

A04:2017 XML外部エンティティ（XXE）¶
XXE攻撃は、XMLパーサーがXMLペイロードのdoctype内にある外部エンティティ宣言を適切に処理しない場合に発生します。

この記事では、.NETの最も一般的なXML処理オプションについて説明しています。

XXEおよびその他のXMLサービス攻撃を防止するための詳細情報については、XXEチートシートを参照してください。

A07:2017 クロスサイトスクリプティング（XSS）¶
ユーザーが送信したデータを信頼しないでください。デニーリストではなく、許可リスト（常に安全）を優先してください。

MVC3では、すべてのHTMLコンテンツがエンコードされます。 HTML、JavaScript、CSS、LDAPなど、すべてのコンテンツを適切にエンコードするには、Microsoft AntiXSSライブラリを使用してください：

Install-Package AntiXSS

次に、構成で次のように設定します：

<system.web>
<httpRuntime targetFramework="4.5"
enableVersionHeader="false"
encoderType="Microsoft.Security.Application.AntiXssEncoder, AntiXssLibrary"
maxRequestLength="4096" />
DO NOT disable Request Validation in ASP.NET Web Forms

次に、白名リストに追加された一連のHTMLタグを確認します。独自のタグを追加するには、AllowHtml属性を使用してください。

ModelStateDictionaryにエラーメッセージを追加する前に、すべてのHTMLをエンコードしてください。

WebFormsおよびMVCの両方で、ユーザーが入力したデータを出力するときは、表示を安全にするためにServer.HtmlEncode（）またはHttpUtility.HtmlEncode（）を使用してください。

For Razor Pages, be sure to use the built-in Razor HTML encoding:

<div>@Model.Name</div>
例えば、一般的なHTMLエンコード攻撃：
<a href="<script>alert('XSS')</script>">Click me</a>
を防ぐには、HtmlAttributeEncode（）メソッドを使用します：

<a href="@Server.HtmlAttributeEncode("<script>alert('XSS')</script>")">Click me</a>
または、MVCでは：

<a href="@HttpUtility.HtmlAttributeEncode("<script>alert('XSS')</script>")">Click me</a>
XSSチートシートには、他のXSS攻撃に関する詳細情報が記載されています。

A08:2017 セキュリティ設定の不備 - SSLを使用しない/適切に構成されていない¶
アプリケーションにおいて、HTTPSプロトコルを常に使用するようにしてください。これは、データがネットワークを介して送信される場合に、暗号化とデータの完全性の保護を提供します。

IISを使用してWebサーバーをホストしている場合、SSL証明書を適切に構成して、通信が暗号化されていることを確認してください。 Let's Encryptなどの無料の証明書オーソリティを使用することができます。

また、HSTS（HTTP Strict Transport Security）ヘッダーを設定して、HTTPSを強制することも重要です。

HTTPにリダイレクトすることで、HTTPSへのリクエストを自動的にリダイレクトできます：

app.UseHttpsRedirection();
さらに、Web.configファイルでHSTSを設定することもできます：

<system.webServer>
<httpProtocol>
<customHeaders>
<add name="Strict-Transport-Security" value="max-age=31536000" />
</customHeaders>
</httpProtocol>
</system.webServer>
A09:2017 未認証データのデータベース¶
ユーザーからのすべての入力を検証して、安全であることを確認してください。不要なデータをデータベースに保存しないでください。

パラメータ化されたクエリまたはORM（Object-Relational Mapping）フレームワークを使用して、SQLインジェクションを防止してください。

動的なクエリを構築する際に文字列の連結を使用しないでください。代わりに、SqlParameterやQueryDSLを使用してください。

A10:2017 インジェクション¶
データベースアクセスにおいて、動的SQLクエリの代わりにパラメータ化されたクエリまたはORM（Object-Relational Mapping）フレームワークを使用してください。

文字列の連結を使用してSQLクエリを構築しないでください。

ユーザーからの入力を受け取る場合は、常に入力を検証して消毒してください。
