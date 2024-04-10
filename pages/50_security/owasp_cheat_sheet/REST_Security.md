概要
REST（またはREpresentational State Transfer）は、最初にRoy FieldingのPh.D.論文である「Architectural Styles and the Design of Network-based Software Architectures」で説明されたアーキテクチャルスタイルです。

FieldingがHTTP/1.1およびURI仕様を書きながら進化し、分散ハイパーメディアアプリケーションの開発に適していることが証明されました。RESTはより広範に適用できますが、HTTP経由でサービスと通信するコンテキストで最も一般的に使用されています。

RESTにおける情報の主要な抽象化はリソースです。REST APIリソースは、通常HTTP URLで識別されます。RESTコンポーネントは、表現を使用してリソースの現在または意図された状態をキャプチャし、その表現を転送することによってリソース上で操作を実行するためのコネクタを使用します。

主要なコネクタの種類はクライアントとサーバーで、セカンダリのコネクタにはキャッシュ、リゾルバ、およびトンネルがあります。

REST APIは状態を持ちません。状態を持つAPIはRESTアーキテクチャルスタイルに準拠していません。RESTの状態とは、APIがアクセスするリソースの状態のことであり、APIが呼び出されるセッションの状態ではありません。状態を持つAPIを構築する理由があるかもしれませんが、セッションを管理することは複雑で安全に行うのが難しいことに気付くことが重要です。

状態を持つサービスはこのチートシートの対象外です。クライアントからバックエンドに状態を渡すことで、サービスを技術的に状態を持たないようにすることは、再生やなりすまし攻撃のリスクがあるため、避けるべき反パターンです。

REST APIを使用してフローを実装するためには、通常、リソースが作成され、読み取られ、更新され、削除されます。たとえば、電子商取引サイトでは、空のショッピングカートを作成するメソッド、カートに商品を追加するメソッド、カートをチェックアウトするメソッドが提供される場合があります。これらの各REST呼び出しは状態を持たず、エンドポイントは呼び出し元が要求された操作を実行する権限があるかどうかを確認する必要があります。

RESTアプリケーションのもう1つの重要な特徴は、標準的なHTTP動詞とエラーコードの使用です。これにより、異なるサービス間の不必要なバリエーションが取り除かれます。

RESTアプリケーションのもう1つの重要な特徴は、HATEOASまたはHypermedia As The Engine of Application Stateの使用です。これにより、RESTアプリケーションは自己文書化され、開発者が事前の知識なしにRESTサービスと対話しやすくなります。

HTTPS
セキュアなRESTサービスは、HTTPSエンドポイントのみを提供する必要があります。これにより、認証資格情報（パスワード、APIキー、またはJSON Webトークンなど）が送信中に保護されます。また、クライアントがサービスを認証し、送信されたデータの整合性を保証します。

詳細については、Transport Layer Security Cheat Sheetを参照してください。

高特権のWebサービスを追加の保護するために相互認証されたクライアントサイド証明書の使用を検討してください。

アクセス制御
非公開のRESTサービスは、各APIエンドポイントでアクセス制御を実行する必要があります。モノリシックアプリケーションのWebサービスは、ユーザー認証、承認ロジック、およびセッション管理によってこれを実装します。これには、RESTfulスタイルに従って複数のマイクロサービスを構成するモダンなアーキテクチャにはいくつかの欠点があります。

レイテンシを最小限に抑え、サービス間の結合を減らすために、アクセス制御の決定はRESTエンドポイントでローカルに行う必要があります。
ユーザー認証は、アクセストークンを発行するIdentity Provider（IdP）で集中管理されるべきです。
JWT
JSON Webトークン（JWT）の形式としての使用に向けて収束が見られます。JWTは、アクセス制御の決定に使用できる一連のクレームを含むJSONデータ構造です。暗号署名またはメッセージ認証コード（MAC）を使用してJWTの整合性を保護できます。

JWTが署名またはMACによって整合性が保護されていることを確認してください。 {"alg":"none"}の安全でないJWTを許可しないでください。
一般的に、JWTの整合性保護には署名がMACよりも好まれるべきです。
MACを整合性保護に使用する場合、JWTを検証できるすべてのサービスが同じキーを使用して新しいJWTを作成することができます。これは、同じキーを使用するすべてのサービスが互いに信頼する必要があることを意味します。これの別の結果は、任意のサービスの妥協が同じキーを共有するすべての他のサービスも妥協させることです。追加情報はこちらを参照してください。

信頼するパーティまたはトークンの消費者は、その整合性と含まれるクレームを検証することによってJWTを検証します。

信頼するパーティは、独自の構成またはハードコードされたロジックに基づいてJWTの整合性を検証する必要があります。 JWTヘッダの情報を使用して検証アルゴリズムを選択しないでください。こちらとこちらを参照してください。
一部のクレームは標準化されており、アクセス制御に使用されるJWTに含まれるべきです。少なくとも次の標準クレームのいずれかが検証されるべきです。

issまたはissuer - これは信頼できる発行者ですか？これは署名キーの予想される所有者ですか？
audまたはaudience - このJWTのターゲットオーディエンスはリレーパーティですか？
expまたは有効期限 - 現在の時刻はこのトークンの有効期間の終了よりも前ですか？
nbfまたはnot before time - 現在の時刻はこのトークンの有効期間の開始後ですか？
JWTには認証されたエンティティ（ユーザーなど）の詳細が含まれているため、セッションが明示的なログアウトまたはアイドルタイムアウトによって有効期限よりも早く終了した場合など、JWTとユーザーの現在のセッションの状態との間に不一致が発生する可能性があります。明示的なセッション終了イベントが発生した場合、関連するJWTのダイジェストまたはハッシュをAPI上の拒否リストに送信し、そのJWTをトークンの有効期限が切れるまでの間、リクエストで無効にします。詳細については、JSON_Web_Token_for_Java_Cheat_Sheetを参照してください。

APIキー
アクセス制御のないパブリックRESTサービスは、過剰な帯域幅やコンピュートサイクルの請求が発生するリスクがあります。このリスクを緩和するために、APIキーを使用できます。また、組織がAPIを収益化するためにAPIキーがよく使用されます。高頻度の呼び出しをブロックする代わりに、クライアントには購入したアクセスプランに応じてアクセスが与えられます。

APIキーは、サービス拒否攻撃の影響を軽減することができます。ただし、サードパーティのクライアントに発行されると、比較的簡単に妥協される可能性があります。

保護されたエンドポイントへのすべてのリクエストにAPIキーを要求してください。
リクエストが速すぎる場合は、429 Too Many Requests HTTP応答コードを返します。
クライアントが使用許諾契約に違反した場合は、APIキーを取り消します。
機密、重要、または高価値のリソースを保護するためにAPIキーだけに頼らないでください。
HTTPメソッドの制限
許可されたHTTPメソッドのホワイトリストを適用します。たとえば、GET、POST、PUTなどです。
ホワイトリストに一致しないすべてのリクエストをHTTP応答コード405 Method not allowedで拒否します。
呼び出し元がリソースコレクション、アクション、およびレコードで着信HTTPメソッドを使用する権限があることを確認してください
特にJava EEでは、これを適切に実装することが難しい場合があります。HTTP Verb TamperingでWeb認証と承認をバイパスする方法の説明については、こちらを参照してください。

入力検証
入力パラメータ/オブジェクトを信頼しないでください。
入力を検証します：長さ/範囲/形式およびタイプ。
APIパラメータで数値、ブール値、日付、時刻、または固定データ範囲などの強力な型を使用することにより、暗黙の入力検証を実現します。
正規表現で文字列入力を制限します。
予期しない/不正なコンテンツを拒否します。
特定の言語のバリデーション/サニタイゼーションライブラリまたはフレームワークを使用します。
適切なリクエストサイズ制限を定義し、制限を超えるリクエストをHTTP応答ステータス413 Request Entity Too Largeで拒否します。
入力検証の失敗をログに記録します。秒間何百もの入力検証の失敗を行う人物は何か悪いことをしていると仮定してください。
包括的な説明のための入力検証チートシートを参照してください。
受信メッセージの解析には安全なパーサーを使用してください。XMLを使用している場合は、XXEや類似の攻撃に対して脆弱性のないパーサーを使用してください。
コンテンツタイプの検証
RESTリクエストまたはレスポンスの本文は、ヘッダーで意図されたコンテンツタイプと一致する必要があります。そうでないと、これによりコンシューマー/プロデューサー側で誤解が生じ、コードのインジェクション/実行が発生する可能性があります。

APIでサポートされているすべてのコンテンツタイプを文書化します。
リクエストコンテンツタイプを検証します
予期しないまたは欠落したコンテンツタイプヘッダーを含むリクエストをHTTP応答ステータス406 Unacceptableまたは415 Unsupported Media Typeで拒否します。
XMLコンテンツタイプの場合は、適切なXMLパーサーハードニングを確認してください。XXEチートシートを参照してください。
XXE攻撃に脆弱性のないXMLパーサーを使用するため、意図しないコンテンツタイプを明示的に定義することにより、XXE攻撃ベクトルを回避します。たとえば、Jersey（Java）@consumes("application/json"); @produces("application/json")。これにより、XXE攻撃ベクトルが回避されます。
安全なレスポンスコンテンツタイプを送信します
RESTサービスでは、複数の応答タイプ（例：application/xmlまたはapplication/json）を許可することが一般的であり、クライアントはリクエストのAcceptヘッダーで優先順位を指定します。

Acceptヘッダーを単にContent-typeヘッダーにコピーしないでください。
Acceptヘッダーに許可されているタイプのいずれかを含んでいない場合、（理想的には406 Not Acceptable応答とともに）リクエストを拒否してください。
スクリプトコード（JavaScriptなど）を含むサービスは、ヘッダーインジェクション攻撃に対して特に注意する必要があります。

レスポンスで意図されたコンテンツタイプヘッダーを送信し、本文コンテンツに一致するようにしてください。たとえば、application/jsonであり、application/javascriptではありません。
管理エンドポイント
インターネット経由で管理エンドポイントを公開しないでください。
管理エンドポイントがインターネット経由でアクセス可能である必要がある場合は、ユーザーが強力な認証メカニズム、例えば多要素認証を使用する必要があります。
異なるHTTPポートまたはホストを介して管理エンドポイントを公開し、可能な限り別のNICおよび制限されたサブネットで制限します。
これらのエンドポイントへのアクセスをファイアウォールルールで制限するか、アクセス制御リストを使用してください。
エラーハンドリング
汎用的なエラーメッセージで応答します-不要な詳細を明示するのは避けてください。
技術的な詳細（例：呼び出しスタックまたはその他の内部ヒント）をクライアントに渡さないでください。
監査ログ
セキュリティ関連のイベントの前後に監査ログを書き込みます。
詳細レベルは、メッセージが妥当であり、正しく検証された場合でも、リクエストヘッダーおよびボディー、レスポンスヘッダーおよびボディー、およびAPIキーのリクエストとレスポンスのペイロードを含む必要があります。
監査ログにはユーザーセッションIDを含めないでください。代わりに、リクエスト/レスポンス間で一貫して匿名のセッションIDを使用してください。
開発およびテストでは、監査ログを使用してテストシナリオを作成および実行します。
デフォルトのログ設定を活用して、重要なエラーまたは警告を追跡します。
アクセスログ
すべてのリクエストおよびレスポンスを記録し、リアルタイムの監視を提供するアクセスログを実装します。アクセスログには次の情報が含まれています。

クライアントIPアドレス
リモートユーザーID
リクエストの日時と時間
リクエストのHTTPメソッド
リクエストのURIパス
リクエストのHTTPステータスコード
返されたペイロードサイズ（バイト）
API呼び出しの処理時間（ミリ秒）
セッション管理
RESTアーキテクチャでは、セッションの状態はクライアントに保持されるべきではありません。クライアントは、状態を含めないリクエストを提供する必要があります。セッションステートを管理する場合は、RESTの基本原則に違反します。

セッションステートを管理する必要がある場合は、クライアントによるREST APIの使用が適していない可能性があります。代わりに、トークンベースの認証システムを実装してください。

すべてのAPIレスポンスでセッションIDを含めないでください。
セッショントークンがAPIリクエストに含まれている場合、サーバーが正しいセッション情報を取得できることを確認してください。
セッショントークンの期限切れを管理し、適切なエラー応答（たとえば、HTTPステータスコード401 Unauthorized）を返します。
すべてのリクエスト/レスポンスボディでセッショントークンを暗号化します。
セッショントークンは機密情報であるため、HTTPSを介したすべての通信で暗号化する必要があります。
参考文献
APIセキュリティ:APIキーの使用
APIセキュリティ:OAuth
APIセキュリティ:一般的な考慮事項
APIセキュリティ:JWT
APIセキュリティ:セッション管理
OWASP APIセキュリティトップ10
The Twelve-Factor App:ログ
参考文献
OWASP REST Security Cheat Sheet
OWASP API Security Top 10
The Twelve-Factor App:Logging
Security Considerations for REST Key Management
Understanding RESTful APIs
Secure Your REST API... The Right Way
REST Security Cheat Sheet by David Washecka & Eric Sheridan is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. Based on a work at https://www.owasp.org/index.php/REST_Security_Cheat_Sheet. Permissions beyond the scope of this license may be available at https://owasp.org.