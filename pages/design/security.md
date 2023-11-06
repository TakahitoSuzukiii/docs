## WAF
- [WAFとは？仕組みや種類、対応する攻撃を分かりやすく解説](https://www.kagoya.jp/howto/engineer/itsystem/waf01/ "WAFとは？仕組みや種類、対応する攻撃を分かりやすく解説")
> WAF（ワフ）とは「Web Application Firewall」の略称で、サイバー攻撃からWebアプリケーションを守るセキュリティ対策の一つです。
- シグネチャの自動更新
- Cookieの保護
- 特定URLの除外や特定IPアドレスの拒否
- ログ収集及びレポート出力
### 対策
> シグネチャ
> スコアリング
> AI（人工知能）
## セキュリティ
### XSS
- [クロスサイトスクリプティングって何？サイトのセキュリティを高めるために](https://www.kagoya.jp/howto/it-glossary/security/xss/ "クロスサイトスクリプティングって何？サイトのセキュリティを高めるために")
> フィッシング詐欺
> セッションハイジャック
> Cookieを盗む攻撃
> ウェブサイトの改ざん
### 対策
> 入力値の制限
> サニタイジング（エスケープ）
> WAF設定
### SQL Injection
- [【初心者向け】SQLインジェクションの概要と対策方法](https://www.kagoya.jp/howto/it-glossary/security/sql-injection/ "【初心者向け】SQLインジェクションの概要と対策方法")
> 対策：原則、プリアードステートメントを使用する
>> サニタイズ、エスケース処理と同じように、文字列を正しく変換（マッピング）し、不正がSQL分が生成されないようにすること
## DoS攻撃/DDoS攻撃
- [DoS攻撃/DDoS攻撃の違いとその対策方法](https://www.kagoya.jp/howto/engineer/infosecurity/dos-ddos/ "DoS攻撃/DDoS攻撃の違いとその対策方法")
> 攻撃対象のサーバーに対し膨大な量のデータを送信し、サーバーに大きな負荷を与え、サービスを停止させるのが目的