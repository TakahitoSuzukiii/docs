# AWS Auto Scaling

- [AWS再入門ブログリレー2022 AWS Auto Scaling 編](https://dev.classmethod.jp/articles/re-introduction-2022-aws-auto-scaling/)
- [AWS再入門2018 Amazon EC2 Auto Scaling編](https://dev.classmethod.jp/articles/2018-aws-re-entering-autoscaling/)

# AWS Auto Scalingとは

対象リソースを簡単にスケーリングして、コストを削減しながらアプリケーションのパフォーマンスを最適化することができるサービス

# 対象のリソース

- Amazon EC2 Auto Scaling グループ
- Amazon Elastic Container Service (ECS) サービス (現時点では、リソースタグによる ECS サービスの識別は行えません)
- Amazon EC2 スポットフリート
- Amazon DynamoDB
- Amazon Aurora の Aurora レプリカ

# スケーリングプラン

**検索対象**からスケーリングプランの作成

## 検索対象

- タグでのリソース指定
- Amazon EC2 Auto Scalingグループの選択
- CloudFormation スタック

# メリット

- すばやく設定
- **スケーリング戦略**によるスマートな決定
- パフォーマンスを自動的に維持
- コストを予測し、無駄を省く

スケーリングのしきい値は、以下の4つのスケーリング戦略

## スケーリング戦略

- 可用性を考えた最適化
- コストに合わせて最適化
- 可用性とコストのバランス
- カスタム

# 料金

無料

# 類似のAuto Scalingサービスとその違い

- **AWS Auto Scaling**
- Amazon EC2 Auto Scaling
- Application Auto Scaling

**AWS Auto Scaling**は、Amazon EC2 Auto ScalingとApplication Auto Scaling等をまとめて管理することができるサービス


# AWS Auto ScalingとAmazon EC2 Auto Scalingの使い分け

> 前提として、個別にコンソールからリソース毎のスケーリングポリシーを設定することも可能

## AWS Auto Scalingの使用が推奨される場合

複数のサービスにまたがる複数のリソースのスケーリングを管理する

## EC2 Auto Scalingの使用が必要となる場合

スケジュールに基づくスケールやステップスケーリングポリシーを指定する場合

> AWS Auto Scalingからは設定が出来ない為[^1]

[^1]: [AWS Auto Scaling に関するよくある質問](https://aws.amazon.com/jp/autoscaling/faqs/)