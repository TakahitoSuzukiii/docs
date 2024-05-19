# セキュリティ

## 脆弱性

コンピューターやソフトウェア、ネットワークが抱える弱点。

## 脆弱性診断

セキュリティ要件を満たしているかテストしたり、脆弱性がないか、調べること

## 脆弱性診断

- [脆弱性診断士スキルマッププロジェクト](https://github.com/OWASP/www-chapter-japan/tree/master/skillmap_project#readme)

## セキュリティ要件

- [Web システム／Web アプリケーションセキュリティ要件書](https://github.com/OWASP/www-chapter-japan/tree/master/secreq#web%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0web%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E8%A6%81%E4%BB%B6%E6%9B%B8)

# Awesome series

- [Awesome Security](https://github.com/sbilly/awesome-security)
- [Awesome Web Security](https://github.com/qazbnm456/awesome-web-security?tab=readme-ov-file#awesome-web-security-)
- [android-security-awesome](https://github.com/ashishb/android-security-awesome?tab=readme-ov-file#android-security-awesome-)

# OWASP

- [【レポート】AWS における安全な Web アプリケーションの作り方 #AWS-55 #AWSSummit](https://dev.classmethod.jp/articles/awssummit-2021-aws-55/)
- [Web アプリケーションの脆弱性とセキュリティガイドライン](https://d1.awsstatic.com/events/jp/2021/summit-online/AWS-55_AWS_Summit_Online_2021_Developing-Secure-Web-Applications-on-AWS.pdf)
- [オープンソースの SCA、SAST、DAST ツールを使用したエンドツーエンドの AWS DevSecOps CI/CD パイプラインの構築](https://aws.amazon.com/jp/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/)
- [ZAPping the OWASP Top 10 (2021)](https://www.zaproxy.org/docs/guides/zapping-the-top-10-2021/)

## セキュリティテスト

- SAST
  静的アプリケーション解析（ソースコード診断）

  - [Source Code Analysis Tools](https://owasp.org/www-community/Source_Code_Analysis_Tools#)

- DAST
  動的アプリケーション解析（動的診断）＝ OWASP ZAP

  ※類似スキャンツール：

  - Burp Suite
  - Nikto
  - Fiddler

  - [Vulnerability Scanning Tools](https://owasp.org/www-community/Vulnerability_Scanning_Tools)

- SCA
  ソフトウェアコンポジション解析

## OWASP Cheat Sheet

- [official](https://cheatsheetseries.owasp.org/)
- [github](https://github.com/OWASP/CheatSheetSeries)
- [Zed Attack Proxy (ZAP) ](https://github.com/zaproxy/zaproxy)

## Series

- [Vulnerability Disclosure Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html)
- [Vulnerable Dependency Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html)
- [Web Service Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html)
- [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [Cloud Architecture Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Cloud_Architecture_Cheat_Sheet.html)
- [SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)
- [Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
- [DotNet Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DotNet_Security_Cheat_Sheet.html)

## Web アプリケーションのセキュリティ

- [OWASP Serverless Top 10](https://owasp.org/www-project-serverless-top-10/)
- [OWASP Proactive Controls](https://owasp.org/www-project-proactive-controls/)
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)

# IPA

## 安全なウ ェ ブ サ イ ト の作り方 改訂第７版

- [安全なウェブサイトの作り方](https://www.ipa.go.jp/security/vuln/websecurity/about.html)

## 共通脆弱性タイプ

- [共通脆弱性タイプ一覧 CWE 概説](https://www.ipa.go.jp/security/vuln/scap/cwe.html)
- [共通脆弱性識別子 CVE 概説](https://www.ipa.go.jp/security/vuln/scap/cve.html)
- [共通脆弱性評価システム CVSS v3 概説](https://www.ipa.go.jp/security/vuln/scap/cvssv3.html)

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

- [WAF とは？仕組みや種類、対応する攻撃を分かりやすく解説](https://www.kagoya.jp/howto/engineer/itsystem/waf01/)
  > WAF（ワフ）とは「Web Application Firewall」の略称で、サイバー攻撃から Web アプリケーションを守るセキュリティ対策の一つです。
- シグネチャの自動更新
- Cookie の保護
- 特定 URL の除外や特定 IP アドレスの拒否
- ログ収集及びレポート出力

## 対策

> シグネチャ
> スコアリング
> AI（人工知能）

# XSS

- [クロスサイトスクリプティングって何？サイトのセキュリティを高めるために](https://www.kagoya.jp/howto/it-glossary/security/xss/)
  > フィッシング詐欺
  > セッションハイジャック
  > Cookie を盗む攻撃
  > ウェブサイトの改ざん

## 対策

> 入力値の制限
> サニタイジング（エスケープ）
> WAF 設定

# SQL Injection

- [【初心者向け】SQL インジェクションの概要と対策方法](https://www.kagoya.jp/howto/it-glossary/security/sql-injection/)
  > 対策：原則、プリアードステートメントを使用する
  >
  > > サニタイズ、エスケース処理と同じように、文字列を正しく変換（マッピング）し、不正が SQL 分が生成されないようにすること

## DoS 攻撃/DDoS 攻撃

- [DoS 攻撃/DDoS 攻撃の違いとその対策方法](https://www.kagoya.jp/howto/engineer/infosecurity/dos-ddos/ "DoS攻撃/DDoS攻撃の違いとその対策方法")
  > 攻撃対象のサーバーに対し膨大な量のデータを送信し、サーバーに大きな負荷を与え、サービスを停止させるのが目的

## Cookie と session

- [cookie と session について](https://zenn.dev/airiswim/articles/3ea83df67edf5d)
