# algorithm

- [Twitter's Recommendation Algorithm](https://github.com/twitter/the-algorithm?tab=readme-ov-file#twitters-recommendation-algorithm)

# ストレージ管理

- [cookie](https://developer.mozilla.org/ja/docs/Web/HTTP/Cookies "cookie")
- [GDPR 対応](https://b-risk.jp/blog/2022/02/gdpr/ "GDPR対応")
- [ローカルストレージ]("ローカルストレージ")
- [セッションストレージ]("セッションストレージ")

# ローカライゼイション

# ページネーション

- [シーク法を使ったアクセス](https://use-the-index-luke.com/ja/sql/partial-results/fetch-next-page#fig07_03 "シーク法を使ったアクセス")
- [カーソルページネーションを実装した話](https://lab.mo-t.com/blog/cursor-pagination-implementation "カーソルページネーションを実装した話")

# 排他制御、mutual exclusion

- [排他制御](https://ja.wikipedia.org/wiki/%E6%8E%92%E4%BB%96%E5%88%B6%E5%BE%A1)
- [mutex](https://ja.wikipedia.org/wiki/%E3%83%9F%E3%83%A5%E3%83%BC%E3%83%86%E3%83%83%E3%82%AF%E3%82%B9)
- [セマフォ](https://ja.wikipedia.org/wiki/%E3%82%BB%E3%83%9E%E3%83%95%E3%82%A9)

- [トランザクションと排他制御(楽観ロック悲観ロック)の基礎知識](https://zenn.dev/airiswim/articles/ebe313fb39a4c9)

## トランザクション

# ACID 特性

- Atomicity: 原子性
  すべての操作が完全に実行されるか、一切実行されないかのどちらかであることを保証する。
- Consistency: 一貫性
  トランザクションの実行前後でデータベースの整合性が保たれること。
- Isolation: 独立性,分離性
  同時に実行されても、トランザクションは互いに影響を及ぼさないこと。
- Durability: 耐久性
  トランザクションが完了した後も、変更は永続的で失われないこと。

## Isolation: 独立性,分離性

影響を受けず独立していること。

→ 対処法はロック（排他制御）をかける。ただし、粒度が大事 → つまり、分離レベルの話になる

### リード現象

- ダーティリード: Dirty Reads
  まだコミットされていない他のトランザクションによって
  変更されたデータを読み取ることができる問題。
- ファジーリード: Non-repeatable reads
  同じトランザクション内で複数回同じクエリを実行すると、
  異なる結果が得られる問題。
- ファントムリード: Phantom reads
  同じクエリを複数回実行した際に、結果に含まれるデータが異なる問題。
  他のトランザクションの挿入や削除によって影響を受ける。

### 分離レベル

別途、参照・・・

### ロック、排他制御

- 楽観ロック
  更新対象のデータが、データ取得時と同じ状態であることを確認してから
  更新することで、データの整合性を保証する手法 - 同じ処理を複数人が同時に実行するケースが少なく、競合が発生しづらい場合
  ユースケース：処理時間が比較的短い処理の場合
  → ロックをかけず、データにバージョンを持たせることでデータの整合性を保証する方法
- 悲観ロック
  更新対象のデータを取得する際に
  ロックをかけることことで他のトランザクションから更新されないようにする手法 - 同じ処理を複数人が同時に実行するケースが多く、競合が発生しやすい場合
  ユースケース：処理時間が長くかかる処理の場合
  → ロックをかけて（更新対象のデータ=レコード）、他のトランザクションから更新されないようにする

  ※デッドロック
  同一トランザクション内で複数のレコードを更新するとデッドロックが発生する
  つまり、2 つの資源が待機状態（ロックされている）のため、処理が進まない

# 認証・認可・ブロック機能

- [認可・権限管理の基礎概念](https://masatora.net/blogs/%E8%AA%8D%E5%8F%AF%E3%83%BB%E6%A8%A9%E9%99%90%E7%AE%A1%E7%90%86%E3%81%AE%E5%9F%BA%E7%A4%8E)
- [属性ベースのアクセス制御（ABAC）とは？ メリットと適切なアクセス制御モデル](https://www.okta.com/jp/blog/2020/09/attribute-based-access-control-abac/)

# OAuth2.0

- [一番分かりやすい OAuth の説明](https://qiita.com/TakahikoKawasaki/items/e37caf50776e00e733be)
- [OAuth 2.0 全フローの図解と動画](https://qiita.com/TakahikoKawasaki/items/200951e5b5929f840a1f#%E3%81%BE%E3%81%A8%E3%82%81)

# SAML2.0

- [SAML-tracer](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [SAML, WS-Federation and OAuth 2.0 tracer](https://microsoftedge.microsoft.com/addons/detail/saml-wsfederation-and-o/boffpaecgbbojpkboijhbmhecoefdehi)

# Google

- [Google zanzibar](https://www.osohq.com/learn/google-zanzibar)

# OpenID Connect, OICD

- [一番分かりやすい OpenID Connect の説明](https://qiita.com/TakahikoKawasaki/items/498ca08bbfcc341691fe)

# JSON Web Token (JWT)

- [JSON Web Token (JWT)](https://qiita.com/TakahikoKawasaki/items/8f0e422c7edd2d220e06#6-json-web-token-jwt)

# authlete

- [authlete](https://qiita.com/search?sort=&q=authlete)
- [認可のアーキテクチャに関する考察](https://zenn.dev/she_techblog/articles/6eff1f28d107be "認可のアーキテクチャに関する考察")
- [uuac](https://inria.hal.science/hal-01534764/document)
- [uuac](https://inria.hal.science/hal-01284863/document)
- [auth0](https://auth0.com/jp)
- [freee の権限管理基盤マイクロサービスの今を語ろう！](https://developers.freee.co.jp/entry/authorization-management-microservice)

# 決済機能

- [外部決済サービスを利用する上での脆弱ポイントと対策 #devio2022](https://dev.classmethod.jp/articles/devio2022-vulnerable-points-and-countermeasures-for-using-external-payment-services/)
- [外部決済サービスを利用した開発の反省と改善 #devio2021](https://dev.classmethod.jp/articles/devio2021-introspection-and-improvement-of-development-with-external-payment-services/ "外部決済サービスを利用した開発の反省と改善 #devio2021")
- [「EC サイトの決済システムを作るなら知っておきたいこと」というテーマで話をしました #devio2020](https://dev.classmethod.jp/articles/developers-io-2020-connect-day5-payment-development-flow-with-e-commerce-site/ "「ECサイトの決済システムを作るなら知っておきたいこと」というテーマで話をしました #devio2020")
- [ハイヤールーの決済基盤開発において考慮したこと](https://hireroo.io/journal/tech/thinking-about-payment-service-in-hireroo "ハイヤールーの決済基盤開発において考慮したこと")

# stripe

- [overview](https://stripe.com/docs/payments/payment-methods/overview?locale=ja-JP "overview")

# リアルタイム通信

- [双方向通信プロトコルまとめ](https://qiita.com/theFirstPenguin/items/55dd1daa9313f6b90e2f "双方向通信プロトコルまとめ")
- [リアルタイム通信](https://www.ibm.com/docs/ja/was-liberty/zos?topic=overview-real-time-communications "リアルタイム通信")

# メッセージング機能

- [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket "WebSocket")
- [WebPush](https://developer.mozilla.org/ja/docs/Web/API/Push_API "WebPush")

# ビデオ通話機能

- [WebRTC](https://developer.mozilla.org/ja/docs/Web/API/WebRTC_API "WebRTC")
- [WebRTC 概要](https://zenn.dev/yuki_uchida/books/c0946d19352af5/viewer/0e7daa "WebRTC概要")

# web ゲーム開発

- [ウェブ用のゲーム開発入門](https://developer.mozilla.org/ja/docs/Games/Introduction "ウェブ用のゲーム開発入門")
- [【Go/GCP】ライブゲーム「あてっこ！ぷにまるず」を支えるバックエンド技術](https://tech.mirrativ.stream/entry/2023/07/28/100000 "【Go/GCP】ライブゲーム「あてっこ！ぷにまるず」を支えるバックエンド技術")

# 全文検索

- [Wikipedia](https://ja.wikipedia.org/wiki/%E5%85%A8%E6%96%87%E6%A4%9C%E7%B4%A2#:~:text=%E5%85%A8%E6%96%87%E6%A4%9C%E7%B4%A2%EF%BC%88%E3%81%9C%E3%82%93%E3%81%B6%E3%82%93%E3%81%91%E3%82%93,%E6%84%8F%E5%91%B3%E3%81%A7%E4%BD%BF%E7%94%A8%E3%81%95%E3%82%8C%E3%82%8B%E3%80%82 "Wikipedia")
- [デージーネット](https://www.designet.co.jp/ossinfo/elasticsearch/ "デージーネット")
- [Amazon RDS for MySQL と全文検索](https://dev.classmethod.jp/articles/amazon-rds-for-mysql-fulltext-search/ "Amazon RDS for MySQL と全文検索")
- [全文検索エンジン「Elasticsearch」の概要と prismatix での活用事例 #devio2022](https://dev.classmethod.jp/articles/devio2022-elasticsearch-prismatix/ "全文検索エンジン「Elasticsearch」の概要とprismatixでの活用事例 #devio2022")
- [全文検索 SaaS の Algolia を使って、DynamoDB のデータを柔軟に検索する](https://dev.classmethod.jp/articles/algolia-dynamodb-search/ "全文検索SaaSのAlgoliaを使って、DynamoDBのデータを柔軟に検索する")

# 機械学習

# 給与計算

- [ドメインや仕様が複雑な開発をうまくすすめるためにやったこと](https://developers.freee.co.jp/entry/how-to-develop-complex-doamains "ドメインや仕様が複雑な開発をうまくすすめるためにやったこと")

# セキュリティ

- [Security](https://developer.mozilla.org/en-US/docs/Web/Security "Security")

# 管理者機能

- [スマホアプリを作る際に対応しておきたい実装ポイント](https://zenn.dev/unbam/articles/5d977f0d0434ec "スマホアプリを作る際に対応しておきたい実装ポイント")
