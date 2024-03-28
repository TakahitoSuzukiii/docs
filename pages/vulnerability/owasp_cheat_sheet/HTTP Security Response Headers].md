HTTPセキュリティレスポンスヘッダー チートシート¶

概要¶
HTTPヘッダーは、簡単に実装できるWebセキュリティの強化手段です。適切なHTTPレスポンスヘッダーは、クロスサイトスクリプティング、クリックジャッキング、情報漏えいなどのセキュリティ脆弱性を防ぐのに役立ちます。

このチートシートでは、すべてのセキュリティ関連のHTTPヘッダー、推奨される構成、および複雑なヘッダーの参照先について説明します。

セキュリティヘッダー¶
X-Frame-Options¶
X-Frame-Options HTTPレスポンスヘッダーは、ブラウザがページを<frame>、<iframe>、<embed>、または<object>内でレンダリングするかどうかを示すために使用できます。サイトはこれを使用して、コンテンツが他のサイトに埋め込まれないようにし、クリックジャッキング攻撃を回避できます。

サポートされているブラウザでは、Content Security Policy（CSP）frame-ancestorsディレクティブがX-Frame-Optionsを廃止します（出典）。

X-Frame-Optionsヘッダーは、それが含まれるHTTPレスポンスに何かと相互作用するものがある場合にのみ有用です（例：リンク、ボタン）。HTTPレスポンスがリダイレクトまたはJSONデータを返すAPIの場合、X-Frame-Optionsはセキュリティを提供しません。

推奨事項¶
可能な限りContent Security Policy（CSP）frame-ancestorsディレクティブを使用します。

ページをフレーム内に表示しないようにします。

X-Frame-Options: DENY

X-XSS-Protection¶
HTTP X-XSS-Protectionレスポンスヘッダーは、Internet Explorer、Chrome、およびSafariの機能であり、反射型クロスサイトスクリプティング（XSS）攻撃を検出するとページの読み込みを停止します。

警告：このヘッダーは、古いWebブラウザを使用しているユーザーをCSPがまだサポートしていない場合に役立ちますが、場合によってはこのヘッダーが安全なウェブサイトでXSSの脆弱性を作成する可能性があります（出典）。

推奨事項¶
インラインJavaScriptの使用を無効にするContent Security Policy（CSP）を使用します。

このヘッダーを設定しないか、明示的にオフにします。

X-XSS-Protection: 0

詳細についてはMozilla X-XSS-Protectionを参照してください。

X-Content-Type-Options¶
X-Content-Type-OptionsレスポンスHTTPヘッダーは、サーバーがブラウザーに、Content-Typeヘッダーで宣伝されているMIMEタイプをフォローし、推測しないようにすることを示します。

このヘッダーは、ブラウザのMIMEタイプのスニッフィングをブロックするために使用されます。これにより、実行可能なMIMEタイプに非実行可能なMIMEタイプが変換される可能性があるMIME混同攻撃が防止されます。

推奨事項¶
サイト全体でContent-Typeヘッダーを正しく設定します。

X-Content-Type-Options: nosniff

Referrer-Policy¶
Referrer-Policy HTTPヘッダーは、リクエストとともに送信されるリファラーヘッダーを含めるべきかどうかを制御します。

推奨事項¶
リファラーポリシーは2014年以降、ブラウザによってサポートされています。現代のブラウザのデフォルト動作は、全てのリファラー情報（オリジン、パス、クエリ文字列）を同じサイトに送信せず、他のサイトにはオリジンのみを送信するようになっています。ただし、すべてのユーザーが最新のブラウザを使用しているわけではないため、この動作を強制するためにすべてのレスポンスでこのヘッダーを送信することをお勧めします。

Referrer-Policy: strict-origin-when-cross-origin

注意：このヘッダーの構成についての詳細はMozilla Referrer-Policyを参照してください。