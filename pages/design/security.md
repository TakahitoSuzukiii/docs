# セキュリティ
## 脆弱性
コンピューターやソフトウェア、ネットワークが抱える弱点。
## 脆弱性診断
セキュリティ要件を満たしているかテストしたり、脆弱性がないか、調べること

## 脆弱性診断
- [脆弱性診断士スキルマッププロジェクト](https://github.com/OWASP/www-chapter-japan/tree/master/skillmap_project#readme)
## セキュリティ要件
- [Webシステム／Webアプリケーションセキュリティ要件書](https://github.com/OWASP/www-chapter-japan/tree/master/secreq#web%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0web%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E8%A6%81%E4%BB%B6%E6%9B%B8)

# Awesome series
- [Awesome Security](https://github.com/sbilly/awesome-security)
- [Awesome Web Security](https://github.com/qazbnm456/awesome-web-security?tab=readme-ov-file#awesome-web-security-)
- [android-security-awesome](https://github.com/ashishb/android-security-awesome?tab=readme-ov-file#android-security-awesome-)

# OWASP
## OWASP Cheat Sheet
- [official](https://cheatsheetseries.owasp.org/)
- [github](https://github.com/OWASP/CheatSheetSeries)
## Series
- [Vulnerability Disclosure Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html)
- [Vulnerable Dependency Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html)
- [Web Service Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html)
- [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [Cloud Architecture Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Cloud_Architecture_Cheat_Sheet.html)
- [SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)
- [Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
- [DotNet Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DotNet_Security_Cheat_Sheet.html)

# IPA
- [共通脆弱性タイプ一覧CWE概説](https://www.ipa.go.jp/security/vuln/scap/cwe.html)
- [共通脆弱性識別子CVE概説](https://www.ipa.go.jp/security/vuln/scap/cve.html)
- [共通脆弱性評価システムCVSS v3概説](https://www.ipa.go.jp/security/vuln/scap/cvssv3.html)
- [安全なウェブサイトの作り方](https://www.ipa.go.jp/security/vuln/websecurity/about.html)

# CWE
- [CWE](https://cwe.mitre.org)
- [JVN Japan Vulnerability Notes](https://jvn.jp/index.html)

# CVE
- [CVE](https://cve.mitre.org/)

# CVSS
- [CVSS (Common Vulnerability Scoring System) Calculator](https://github.com/cvssjs/cvssjs?tab=readme-ov-file)

# Google
- [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)

# WAF
- [WAFとは？仕組みや種類、対応する攻撃を分かりやすく解説](https://www.kagoya.jp/howto/engineer/itsystem/waf01/)
> WAF（ワフ）とは「Web Application Firewall」の略称で、サイバー攻撃からWebアプリケーションを守るセキュリティ対策の一つです。
- シグネチャの自動更新
- Cookieの保護
- 特定URLの除外や特定IPアドレスの拒否
- ログ収集及びレポート出力
## 対策
> シグネチャ
> スコアリング
> AI（人工知能）
# XSS
- [クロスサイトスクリプティングって何？サイトのセキュリティを高めるために](https://www.kagoya.jp/howto/it-glossary/security/xss/)
> フィッシング詐欺
> セッションハイジャック
> Cookieを盗む攻撃
> ウェブサイトの改ざん
## 対策
> 入力値の制限
> サニタイジング（エスケープ）
> WAF設定
# SQL Injection
- [【初心者向け】SQLインジェクションの概要と対策方法](https://www.kagoya.jp/howto/it-glossary/security/sql-injection/)
> 対策：原則、プリアードステートメントを使用する
>> サニタイズ、エスケース処理と同じように、文字列を正しく変換（マッピング）し、不正がSQL分が生成されないようにすること
## DoS攻撃/DDoS攻撃
- [DoS攻撃/DDoS攻撃の違いとその対策方法](https://www.kagoya.jp/howto/engineer/infosecurity/dos-ddos/ "DoS攻撃/DDoS攻撃の違いとその対策方法")
> 攻撃対象のサーバーに対し膨大な量のデータを送信し、サーバーに大きな負荷を与え、サービスを停止させるのが目的