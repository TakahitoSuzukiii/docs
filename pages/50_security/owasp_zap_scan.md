# OWASP ZAP

- [OWASP ZAP のテストを CI/CD に組み込む](https://qiita.com/kemmy-qei/items/ad9c5417eee71277c67f)
- [Docker 版 OWASP ZAP を動かしてみる](https://qiita.com/koujimatsuda11/items/83558cd62c20141ebdda)
- [OWASP ZAP の設定と使い方](https://qiita.com/sangi/items/ba7e3d39237045c9be36)
- [Docker 版 OWASP ZAP を使用して Web アプリの簡易的な脆弱性診断をしてみた](https://dev.classmethod.jp/articles/easy-vulnerability-diagnosis-of-web-app-with-owasp-zap-on-docker/)
- [侵入テスト（AWS）](https://aws.amazon.com/jp/security/penetration-testing/)

## 手順 v2

### 参考

- [Docker や ECR, ECS, Fargate など、コンテナ周りの AWS 知識を効率的にキャッチアップしたい人のために](https://qiita.com/nyandora/items/0fa064f8a4402939673b)
- [Amazon ECS で使用するコンテナイメージの作成　](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/create-container-image.html#use-ecr)
- [Amazon Elastic Container Service とは](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/Welcome.html)
- [Amazon EC2 Container Service(ECS)の概念整理](https://qiita.com/NewGyu/items/9597ed2eda763bd504d7)
- [Docker & Docker-Compose の基本的な使い方](https://qiita.com/koka/items/3d3d4ee5680f92a0ad89)
- [[年末年始にやってみよう]DockerDesktop でイメージ管理を行いながら Docker の知見を高めてみる](https://dev.classmethod.jp/articles/play-docker-with-dockerdesktop/)

1. Docker イメージを作成する

### Dockerfile

- [Dockerfile の ENTRYPOINT と CMD の違いは何でしょうか。](https://qiita.com/Thang_TQ/items/acad14dbbc0500fc9d5f)

```
FROM owasp/zap2docker-stable

# ZAPのデフォルトコンフィグ
COPY zap.conf /zap/

# エントリーポイントスクリプトを追加
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ZAPポート
EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]
```

### ベアリリース（非常に小さな Docker イメージ、ZAP の実行に必要な依存関係のみが含まれ、CI 環境に最適）

```
docker pull owasp/zap2docker-bare
```

### entrypoint.sh ※再検討・要見直し箇所

- [ZAP CLI](https://github.com/Grunny/zap-cli)
- [Command Line](https://www.zaproxy.org/docs/desktop/cmdline/)

```
#!/bin/bash

# スキャン対象のURLを指定
TARGET_URL=${TARGET_URL:-"http://example.com"}

# ZAPをデーモンモードで起動
zap.sh -daemon -host 0.0.0.0 -port 8080 -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true

# スキャン開始
zap-cli -p 8080 quick-scan --self-contained --start-options '-config api.addrs.addr.name=.* -config api.addrs.addr.regex=true' $TARGET_URL

# スキャン結果をレポート
zap-cli -p 8080 report -o /zap/report/report.html -f html

# コンテナを保持（デバッグ用、必要に応じて削除可能）
tail -f /dev/null
```

#### api.addrs.addr.name

- ZAP の API アクセスを許可するアドレスを指定します。
- `=.\*` は、すべてのアドレスからのアクセスを許可する正規表現です。

#### api.addrs.addr.regex

- API アクセスを許可するアドレスリストにおいて正規表現を使用するかどうかを指定します。
- true は、正規表現を有効にする設定です。

### zap.conf ※再検討・要見直し箇所

```
# API アクセス設定
api.addrs.addr.name=.*
api.addrs.addr.regex=true

# プロキシ設定
connection.proxy.enabled=true
connection.proxy.host=proxy.example.com
connection.proxy.port=8080

# スキャン設定
spider.maxDepth=5
spider.maxDuration=60
spider.threadSleep=5000

# レポート設定
reports.directory=/zap/report/
reports.format=html
```

1. Docker イメージをビルドする

### コマンド

```
docker build -t owasp-zap-scanner-dev .
```

3. Docker イメージを ECR に Push する

- [ECR リポジトリにプッシュしたイメージを ECS Fargate で起動する](https://dev.classmethod.jp/articles/amazon-ecr-ecs-fargate/)

```
aws ecr create-repository --vulnerability-scan owasp-zap-scanner-dev
```

### repository-name = Vulnerability Scan

4. ECR にログイン

```
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin [account-id].dkr.ecr.ap-northeast-1.amazonaws.com
```

5. Docker イメージにタグを付ける

```
docker tag owasp-zap-scanner-dev:latest [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/owasp-zap-scanner-dev:latest
```

6. Docker イメージを Push する

```
docker push [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/owasp-zap-scanner-dev:latest
```

7. AWS の環境を準備する

- [AWS Fargate 環境を構築してデプロイしてみる](https://zenn.dev/ttani/articles/aws-fargate-setup)

  1.  VPC を作成
      1. owasp-zap-scanner-dev-vpc を作成する
  2.  Subnet を作成
      1. owasp-zap-scanner-dev-sbn-public-1a、owasp-zap-scanner-dev-sbn-public-1c
  3.  IGW を作成
      1. owasp-zap-scanner-dev-igw
  4.  ルートテーブルを作成
      1. owasp-zap-scanner-dev-public-rt
  5.  ロードバランサーを作成
      1. owasp-zap-scanner-dev-alb
  6.  セキュリティグループを作成
      1. owasp-zap-scanner-dev-alb-sg

8. AWS ECS Fargate でタスク定義を作成する

### owasp-zap-scanner-dev-task-definition.json

```
{
  "family": "owasp-zap-scanner-dev-task",
  "networkMode": "awsvpc",
  "containerDefinitions": [
    {
      "name": "owasp-zap-scanner-dev",
      "image": "[account-id].dkr.ecr.ap-northeast-1.amazonaws.com/owasp-zap-scanner-dev:latest",
      "memory": 512,
      "cpu": 256,
      "essential": true,
      "environment": [
        {
          "name": "TARGET_URL",
          "value": "http://example.com"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/owasp-zap-scanner-dev",
          "awslogs-region": "ap-northeast-1",
          "awslogs-stream-prefix": "ecs-owasp-zap-scanner-dev"
        }
      }
    }
  ],
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::your-account-id:role/ecsTaskExecutionRole"
}
```

8. AWS ECS Fargate でタスク定義を登録する

```
aws ecs register-task-definition --cli-input-json file://owasp-zap-scanner-dev-task-definition.json
```

9.  AWS ECS Fargate で ECS クラスターを作成する

```
aws ecs create-cluster --cluster-name owasp-zap-scanner-dev-cluster
```

10. AWS ECS Fargate でサービスを作成する

```
aws ecs create-service --cluster owasp-zap-scanner-dev-cluster --service-name owasp-zap-scanner-dev-service --task-definition owasp-zap-scanner-dev-task --desired-count 1 --launch-type FARGATE --network-configuration "awsvpcConfiguration={subnets=[subnet-id],securityGroups=[security-group-id],assignPublicIp=ENABLED}"
```

## 手順 v1

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
