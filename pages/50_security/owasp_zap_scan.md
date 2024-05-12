# OWASP ZAP

- [OWASP ZAP のテストを CI/CD に組み込む](https://qiita.com/kemmy-qei/items/ad9c5417eee71277c67f)
- [Docker 版 OWASP ZAP を動かしてみる](https://qiita.com/koujimatsuda11/items/83558cd62c20141ebdda)
- [OWASP ZAP の設定と使い方](https://qiita.com/sangi/items/ba7e3d39237045c9be36)
- [Docker 版 OWASP ZAP を使用して Web アプリの簡易的な脆弱性診断をしてみた](https://dev.classmethod.jp/articles/easy-vulnerability-diagnosis-of-web-app-with-owasp-zap-on-docker/)
- [侵入テスト（AWS）](https://aws.amazon.com/jp/security/penetration-testing/)

## 環境構築

- [【2024 年最新】Window に「Docker」の環境構築](https://zenn.dev/felmy/articles/108c3c30ab7d86)
- [Windows 11 に Docker Desktop を入れる手順（令和 5 年最新版）](https://qiita.com/zembutsu/items/a98f6f25ef47c04893b3)

## start

```
chmod +x start_scan.sh
```

## start_scan.sh

```
#!/bin/bash

docker-compose up -d
docker-compose exec zap zap-baseline.py \
  -t https://www.example.com \
  -g config_file \
  -r ./report.html \
  -w ./report.md
docker-compose down
```

ためす

```
-c config_file: 警告をINFO、IGNORE、FAILのいずれかに設定するための設定ファイルを指定します。
-m mins: スパイダリングの期間を分単位で指定します。デフォルトは1分です。

-g gen_file: デフォルトの設定ファイルを生成し、すべてのルールをWARNに設定します。
-D: パッシブスキャンの待ち時間を秒単位で指定します。
-T: ZAPの起動およびパッシブスキャンの実行までの最大時間を指定します。
```

- [Command Line](https://www.zaproxy.org/docs/desktop/cmdline/)

## docker-compose.yml

```
version: '3.8'

services:
  zap:
    image: owasp/zap2docker-stable
```

### ベアリリース（非常に小さな Docker イメージ、ZAP の実行に必要な依存関係のみが含まれ、CI 環境に最適）

```
docker pull owasp/zap2docker-bare
```
