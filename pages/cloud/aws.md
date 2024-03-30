# Awesome

- [Awesome AWS](https://github.com/donnemartin/awesome-aws#awesome-aws- "Awesome AWS")
- [Awesome AWS ECS](https://github.com/nathanpeck/awesome-ecs#readme "Awesome AWS ECS")
- [Awesome AWS Amplify](https://github.com/dabit3/awesome-aws-amplify#readme "Awesome AWS Amplify")

# Roadmap

- [Roadmap AWS Best Practices](https://roadmap.sh/best-practices/aws)

# classmethod

- [AWS再入門2022](https://dev.classmethod.jp/referencecat/aws-re-introduction-2020-2 "AWS再入門2022")
- [CloudFormation入門](https://dev.classmethod.jp/articles/sainyumon-cloudformation/ "CloudFormation入門")
- [AWS CDK ベストプラクティス](https://aws.amazon.com/jp/blogs/news/best-practices-for-developing-cloud-applications-with-aws-cdk "AWS CDK ベストプラクティス")

# metrics

- [CloudWatch Metricsを利用した監視の基本](https://zenn.dev/tatsuo48/articles/8f436c4a057961 "CloudWatch Metricsを利用した監視の基本")
- [パーセンタイル](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Percentiles "パーセンタイル")
- [インスタンスメトリクス](https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html#ec2-cloudwatch-metrics "インスタンスメトリクス")
- [Application Load Balancer](https://docs.aws.amazon.com/ja_jp/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html "Application Load Balancer")
- [Amazon ECS Container Insights メトリクス](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html "Amazon ECS Container Insights メトリクス")
- [Amazon Aurora](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html "Amazon Aurora")

# cloud formation

- [入門 AWS CloudFormation #1（EC2関係とYAMLの復習編）](https://qiita.com/simonritchie/items/330391e741f394897550)
- [入門 AWS CloudFormation #2（EC2のセキュリティグループ編）](https://qiita.com/simonritchie/items/a1922199a5b6d131dca9)
- [入門 AWS CloudFormation #3（EC2とパラメータ編）](https://qiita.com/simonritchie/items/8b1c3046474ca7c6863c)
- [入門 AWS CloudFormation #4（組み込み関数編）](https://qiita.com/simonritchie/items/5163abaf516902a55f30)
- [入門 AWS CloudFormation #5（条件設定編）](https://qiita.com/simonritchie/items/45f53b1f3b67303a751d)
- [入門 AWS CloudFormation #6（出力とエクスポート、及びそれらの別テンプレートでの利用編）](https://qiita.com/simonritchie/items/2dc2b581f50a823861e9)

# AWS AWS Auto Scaling

アプリケーションの負荷に応じて自動的にリソースをスケーリングするためのサービス

## Auto Scalingグループ

複数のEC2インスタンスをグループ化し、リソースの動的な増減を管理する

### グループ設定

| 項目名                                                                    | 説明                                                                                                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 起動設定（Launch Configuration）または起動テンプレート（Launch Template） | 新しいインスタンスを起動する際に使用される設定。AMI（Amazon Machine Image）、インスタンスタイプ、セキュリティグループ、ユーザーデータなどが含まれ |
| 最小サイズ（Minimum Size）                                                | グループ内に常に存在する最小のインスタンス数                                                                                                      |
| 最大サイズ（Maximum Size）                                                | グループ内のインスタンス数の最大値                                                                                                                |
| 希望サイズ（Desired Capacity）                                            | Auto Scalingグループが保持する希望するインスタンス数                                                                                              |

### スケーリングトリガー

| 項目名                              | 説明                                                                                                                        | 
| ------------------------ | ------------------------ | 
| スケールアウト（Scale Out）トリガー | 負荷が増加した場合に新しいインスタンスを追加するトリガー。CPU利用率、ネットワークトラフィックなどの指標が閾値を超えると発動 | 
| スケールイン（Scale In）トリガー    | 負荷が減少した場合にインスタンスを減らすトリガー。CPU利用率、ネットワークトラフィックなどの指標が閾値を下回ると発動         | 

# AWS Elastic Beanstalk

- [AWS再入門ブログリレー2022 AWS Elastic Beanstalk編](https://dev.classmethod.jp/articles/2022_elasticbeanstalk_introduction/)

## 概要

AWS Elastic Beanstalk は、Java、.NET、PHP、Node.js、Python、Ruby、Go および Docker を使用して開発されたウェブアプリケーションやサービスを、Apache、Nginx、Passenger、IIS など使い慣れたサーバーでデプロイおよびスケーリングするためのサービス

## 特徴

- ウェブサーバー環境
- ワーカー環境

## 特徴

- デプロイの多様な選択肢
- 統一されたユーザーインターフェイスによるモニタリングと管理
- 管理された更新を使用して、最新のプラットフォームバージョンや新しいパッチを自動的に取得できる
- ELBとAuto Scalingを使用して、拡張/縮小ニーズに基づいてアプリケーションを自動的にスケール
- スポットインスタンスやEC2インスタンスタイプなど、アプリケーションにとって最適なAWSリソース選択できる
- 多彩なアプリケーションプラットフォーム？？

## 作成

- 管理されたプラットフォーム
- カスタムプラットフォーム

## 構成

- アプリケーションと環境

> **アプリケーション**の役割はアプリケーションのアップロード（バージョン管理している）と管理
> **環境**の役割は実際の稼働環境

## アプリケーションの作成の流れ

1. アプリケーション名と説明を入力し、アプリケーションを作成する
2. 環境を作成する
   1. 環境（ウェブサーバー/ワーカー）のタイプを選択する
   2. 環境名やドメイン、説明を入力しする
   3. プラットフォームとデプロイするアプリケーションを選択し、環境を作成する
      1. 「より多くのオプションの設定」ボタンから、より詳細な設定ができる

### 設定可能な詳細な設定項目

| ソフトウェア             | プロキシサーバの種類、AWS X-Ray、ログ出力（S3やCloudWatch Logs ）、環境プロパティ                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| インスタンス             | ルートボリュームのタイプ、サイズ、EC2インスタンスのセキュリティグループ                                                  |
| 容量                     | Auto Scaling グループ設定（フリート構成、インスタンスタイプ、AMI ID、AZ配置）、スケーリングトリガー                      |
| ロードバランサー         | ロードバランサーの種類、リスナー、プロセス、ルール、ログ保存設定                                                         |
| ローリング更新とデプロイ | アプリケーションのデプロイメントポリシー、設定の更新方法、ヘルスチェックの要件とデプロイメントタイムアウトのカスタマイズ |
| セキュリティ             | サービスロール、EC2のキーペアやIAMロールの設定                                                                           |
| モニタリング             | ヘルスレポートの設定、ヘルスモニタリングルールのカスタマイズ、CloudWatch Logs へのヘルスイベントのストリーミング         |
| 管理された更新           | 定期的にプラットフォームを自動更新するかの設定、更新レベル、メンテナンスウィンドウの時間帯                               |
| 通知                     | 環境からの重要イベントを受け取るメールアドレスを指定                                                                     |
| ネットワーク             | 使用するVPC、ELBやインスタンス、データベースが使用するサブネット                                                         |
| データベース             | RDSのデータベースを設定（DBエンジン、インスクラス、ストレージ、MultiAZ）、DB削除ポリシー                                 |
| タグ                     | 環境内のリソースにタグを付与                                                                                             |

### ローリング更新とデプロイ

既存環境に新たなアプリケーションをデプロイしたときにどのように反映させるか、既存環境のインフラ設定を変更したときにどのように設定変更するかを定義するもの

#### 種類

- 1回にすべて（All at once）
- ローリング（Rolling）
- 追加バッチとローリング（Rolling with additional batch）
- 変更不可（Immutable）
- トラフィックの分割（Traffic splitting ：ALBのみ使用可能、NLBやCLBでは使用不可）

> **ユーザーへの影響の少ないデプロイとデプロイ速度から選定？**

[AWS Elastic Beanstalkで使えるデプロイポリシーを理解する](https://dev.classmethod.jp/articles/elastic-beanstalk-deploy-policy/)

### Elastic Beanstalkを使用したブルーグリーンデプロイメント

デプロイポリシーとは別の機能でブルーグリーンデプロイメントを実行でき、それが**環境URLのスワップ**

>**環境URLのスワップ**とは環境作成時に割り当てた環境URLを入れ替えるもの

## EB CLI

Elastic Beanstalk専用のコマンドラインツール。他にもAWS CLIやSDKも使える

## その他、デプロイ設定

いろいろ

## モニタリング

モニタリングのダッシュボードから確認

## ヘルスレポート

| 色       | 説明                                                                                                                              | 
| -------- | --------------------------------------------------------------------------------------------------------------------------------- | 
| グレー   | 環境が更新中です                                                                                                                  | 
| グリーン | 環境が最新のヘルスチェックで合格になりました。環境内の少なくとも 1 つのインスタンスが使用可能であり、リクエストを受け取っています | 
| イエロー | 対象環境が 1 つ以上のヘルスチェックで失格になりました。環境へのいくつかのリクエストが失敗しています                               | 
| レッド   | 対象環境が 3 つ以上のヘルスチェックで失格になったか、環境のリソースが使用不可になっています。リクエストは一貫して失敗しています   | 

## アプリケーションのアップロードとデプロイの流れ

1. アプリケーションのバージョン（バージョンラベル）を入力し、war/zipファイルをアップロードする
2. アプリケーションのバージョン（バージョンラベル）を選択し、環境を入力してデプロイする

### サンプル
- [elastic-beanstalk-samples](https://github.com/awsdocs/elastic-beanstalk-samples?tab=readme-ov-file)
- [aws-cognito-angular-quickstart](https://github.com/amazon-archives/aws-cognito-angular-quickstart)
- [go-beanstalk-gin](https://github.com/sudo-suhas/go-beanstalk-gin?tab=readme-ov-file)

##

# 資格

- [約1ヶ月でAWS認定資格を10個取得したエンジニアの学習法まとめ](https://dev.classmethod.jp/articles/aws-certifications-study-methods/)
