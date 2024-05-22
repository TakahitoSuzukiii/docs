# Amazon Cognito

- [AWS 再入門ブログリレー 2022 Amazon Cognito 編](https://dev.classmethod.jp/articles/re-introduction-2022-amazon-cognito/)
- [よくわかる認証と認可](https://dev.classmethod.jp/articles/authentication-and-authorization/#return-note-184783-1)
- [AWS 再入門ブログリレー Amazon Cognito 編](https://dev.classmethod.jp/articles/re-introduction-2020-amazon-cognito/)

- [一番分かりやすい OAuth の説明](https://qiita.com/TakahikoKawasaki/items/e37caf50776e00e733be)
- [一番分かりやすい OpenID Connect の説明](https://qiita.com/TakahikoKawasaki/items/498ca08bbfcc341691fe)

# AWS SDK

- [Welcome](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/Welcome.html)
- [AdminSetUserPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.html)
- [GlobalSignOut](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GlobalSignOut.html)
- [Amazon Cognito ユーザープール API とユーザープールの使用 エンドポイント](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## 認証トークンを使用

- [ChangePassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ChangePassword.html)
- [ForgotPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.html)
- [ConfirmForgotPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmForgotPassword.html)

## .NET

- [AmazonCognitoIdentityProviderClient](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CognitoIdentityProvider/TCognitoIdentityProviderClient.html)

## ユーザープール

複数のメールアドレスとパスワードの設定
1 人のユーザーに対して複数のメールアドレスとパスワードを設定することはできません。

- [ユーザープール属性](https://docs.aws.amazon.com/ja_jp/cognito/latest/developerguide/user-pool-settings-attributes.html)
- [Amazon Cognito とは](https://docs.aws.amazon.com/ja_jp/cognito/latest/developerguide/what-is-amazon-cognito.html)

複数の SAML ベースのプロバイダーの設定
1 人のユーザーに対して複数の SAML IdP を設定することが可能です。

- [ユーザープールの ID プロバイダーの設定](https://docs.aws.amazon.com/ja_jp/cognito/latest/developerguide/cognito-user-pools-identity-provider.html)
- [ユーザープールでの SAML ID プロバイダーの使用](https://docs.aws.amazon.com/ja_jp/cognito/latest/developerguide/cognito-user-pools-saml-idp.html)
