# Awesome

- [Git and Git Flow Cheat Sheet](https://github.com/arslanbilal/git-cheat-sheet#git-and-git-flow-cheat-sheet- "Git and Git Flow Cheat Sheet")

# Git

- [よく使う Git コマンド 19 選！使い方を初心者向けにわかりやすく解説](https://www.sejuku.net/blog/5816#index_id5)

##　 stash

```
git stash save -u コメント
git stash list
git stash apply stash@{0}
git stash drop stash@{0}
git diff stash@{0}
git diff stash@{0} hoge.txt
git stash clear
```

##　 fetch

- [共同開発の第一歩!git fetch を正しく理解しよう!](https://www.sejuku.net/blog/71164)
  > みんなの更新内容を、自分の開発環境に取り入れる機能

```
git fetch
git fetch origin // 特定のリポジトリのみ取得
git fetch --all // 全て取得
git fetch -t // タグの同期
git fetch -p // 削除ブランチの同期
```

## merge

- [git merge でブランチをマージしよう!いろんな疑問を徹底解説](https://www.sejuku.net/blog/71003)
  > 現在のブランチ(HEAD の指している場所)へ、他のブランチの更新を取り込む処理

```
git merge 取り込みたいブランチ
git merge --no-ff 取り込みたいブランチ名 // 強制的にマージコミットを作成するコマンド
```

## pull

- [【Git 入門】pull でリモートリポジトリの履歴に更新する方法](https://www.sejuku.net/blog/70851)
  > 内部で「fetch コマンド」と「merge コマンド」を順次行ってくれているコマンド

```
git pull [リポジトリ名] [ブランチ名]
git pull origin master
```

## reset

```
git reset --hard HEAD^ // git pullの取り消し
```

## rebase

- [これで完璧! 図解でわかる git rebase の 2 つの使い方!](https://www.sejuku.net/blog/71919)
  > 指定したコミットを、ブランチを変えて作り直したり、ひとまとめにしたりして、ログを綺麗にするコマンド
  > merge と rebase の違い：既存のコミットへ影響を与えるか・与えないか

```
git rebase [つなぐ元にするブランチ名]
git rebase -i [ひとまとめにする地点の一つ前のコミットID] // 複数ブランチをまとめるコマンド
```

## auth

- [【Git】personal access token を使用して GitHub へアクセスする and source tree](https://qiita.com/YuukiYoshida/items/2e6b250d44bf1e0f5a0b)
- [GitHub への認証について](https://docs.github.com/en/enterprise-server@3.6/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)
- [個人のアクセストークンの管理](https://docs.github.com/en/enterprise-server@3.6/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [アクセストークン認証](https://zenn.dev/technicarium/articles/5bf0647056fb87#%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%83%88%E3%83%BC%E3%82%AF%E3%83%B3%E8%AA%8D%E8%A8%BC)
- [OAuth アプリのスコープ](https://docs.github.com/ja/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes)

## branch

- [Upstream branch](https://qiita.com/djkazunoko/items/373363648d2e0b620bf8 "Upstream branch")

## Notifications

- [通知](https://zenn.dev/siketyan/articles/you-are-not-using-github-correctly "通知")

## flow

- [Git 2.27 での git pull 時の warning について](https://qiita.com/tearoom6/items/0237080aaf2ad46b1963 "Git 2.27 での git pull 時の warning について")
- [git pull すると hint がたくさん出てくる](https://qiita.com/Bjp8kHYYPFq8MrI/items/77f7dfb9c078a3074b7b "git pullするとhintがたくさん出てくる")
- [git pull と git pull --rebase の違い](https://qiita.com/Hashimoto-Noriaki/items/6e183f738289cf288b23 "git pullとgit pull --rebaseの違い")
- [git pull の取り消し方法をケース別に紹介](https://ensei1375.com/git-pull-reset/ "git pullの取り消し方法をケース別に紹介")

## Gitflow

- [Gitflow ワークフロー](https://www.atlassian.com/ja/git/tutorials/comparing-workflows/gitflow-workflow "Gitflow ワークフロー")
- [Git-flow をざっと整理してみた](https://dev.classmethod.jp/articles/introduce-git-flow "Git-flowをざっと整理してみた")

## GithubOrganization

- [Github Organization おすすめ初期設定](https://tech.cm-group.co.jp/posts/github-organization "Github Organizationおすすめ初期設定")

## GitHubActions

- [GitHubActions](https://github.co.jp/features/actions "GitHubActions")
- [GitHub Actions を使ったマイクロサービスの CI/CD モジュール管理](https://lab.mo-t.com/blog/gha-microservice-cicd "GitHub Actionsを使ったマイクロサービスのCI/CDモジュール管理")
- [【入門】GitHub Actions とは？](https://www.kagoya.jp/howto/it-glossary/develop/githubactions/ "【入門】GitHub Actionsとは？")
- [GitHub の新機能「GitHub Actions」で試す CI/CD](https://knowledge.sakura.ad.jp/23478/ "GitHubの新機能「GitHub Actions」で試すCI/CD")
- [GitHub Actions って何？触ってみて理解しよう！入門・逆引きリファレンス](https://qiita.com/yu-ichiro/items/b50ceb0008edc3c0312e "GitHub Actionsって何？触ってみて理解しよう！入門・逆引きリファレンス")
