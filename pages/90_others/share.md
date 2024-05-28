# vscode

# ユーザースニペット

## setting.json

```
{
    "git.ignoreLimitWarning": true,
    "todo-tree.general.tags": [
        "NOTE",
        "WARNING",
        "TODO",
        "FIXME",
        "BUG",
        "MTG"
    ],
    "todo-tree.highlights.customHighlight": {
        "NOTE": {
            "icon": "note",
            "foreground": "#C0C0C0",
            "iconColour": "#C0C0C0"
        },
        "WARNING": {
            "icon": "alert",
            "foreground": "red",
            "iconColour": "red"
        },
        "TODO": {
            "icon": "check-circle-fill",
            "foreground": "orange",
            "iconColour": "orange"
        },
        "FIXME": {
            "icon": "flame",
            "foreground": "yellow",
            "iconColour": "yellow"
        },
        "BUG": {
            "icon": "bug",
            "foreground": "#40BA8D",
            "iconColour": "#40BA8D"
        },
        "MTG": {
            "icon": "feed-discussion",
            "foreground": "#65BBE9",
            "iconColour": "#65BBE9"
        }
    },
    "editor.tabCompletion": "onlySnippets",
    "[markdown]": {
        "editor.quickSuggestions": true,
    }
}
```

## global.code-snippets

```
{
	// Place your GLOBAL snippets here. Each snippet is defined under a snippet name and has a scope, prefix, body and
	// description. Add comma separated ids of the languages where the snippet is applicable in the scope field. If scope
	// is left empty or omitted, the snippet gets applied to all languages. The prefix is what is
	// used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders.
	// Placeholders with the same ids are connected.
	// Example:
	// "Print to console": {
	// 	"scope": "javascript,typescript",
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"メモ1": {
		"prefix": "め",
		"body": "# NOTE: ",
		"description": "メモ"
	},
	"メモ2": {
		"prefix": "メ",
		"body": "# NOTE: ",
		"description": "メモ"
	},
	"メモ3": {
		"prefix": "me",
		"body": "# NOTE: ",
		"description": "メモ"
	},
	"重要なメモ1": {
		"prefix": "重要",
		"body": "# WARNING: ",
		"description": "重要なメモ"
	},
	"重要なメモ2": {
		"prefix": "じゅ",
		"body": "# WARNING: ",
		"description": "重要なメモ"
	},
	"重要なメモ3": {
		"prefix": "war",
		"body": "# WARNING: ",
		"description": "重要なメモ"
	},
	"やること1": {
		"prefix": "TODO",
		"body": "# TODO: ",
		"description": "やること"
	},
	"やること2": {
		"prefix": "TO",
		"body": "# TODO: ",
		"description": "やること"
	},
	"やること3": {
		"prefix": "や",
		"body": "# TODO: ",
		"description": "やること"
	},
	"修正すること1": {
		"prefix": "FIXME",
		"body": "# FIXME: ",
		"description": "修正すること"
	},
	"修正すること2": {
		"prefix": "FIX",
		"body": "# FIXME: ",
		"description": "修正すること"
	},
	"修正すること3": {
		"prefix": "F",
		"body": "# FIXME: ",
		"description": "修正すること"
	},
	"修正すること4": {
		"prefix": "修正",
		"body": "# FIXME: ",
		"description": "修正すること"
	},
	"修正すること5": {
		"prefix": "しゅ",
		"body": "# FIXME: ",
		"description": "修正すること"
	},
	"バグのことS1": {
		"prefix": "バグ",
		"body": "# BUG: ",
		"description": "バグのこと"
	},
	"バグのことS2": {
		"prefix": "バ",
		"body": "# BUG: ",
		"description": "バグのこと"
	},
	"バグのことS3": {
		"prefix": "ば",
		"body": "# BUG: ",
		"description": "バグのこと"
	},
	"バグのことS4": {
		"prefix": "BUG",
		"body": "# BUG: ",
		"description": "バグのこと"
	},
	"バグのことS5": {
		"prefix": "B",
		"body": "# BUG: ",
		"description": "バグのこと"
	},
	"議事録（日付を追記）1": {
		"prefix": "MTG",
		"body": "# MTG: ",
		"description": "議事録（日付を追記）"
	},
	"議事録（日付を追記）2": {
		"prefix": "M",
		"body": "# MTG: ",
		"description": "議事録（日付を追記）"
	},
	"議事録（日付を追記）3": {
		"prefix": "み",
		"body": "# MTG: ",
		"description": "議事録（日付を追記）"
	},
	"議事録（日付を追記）4": {
		"prefix": "定例",
		"body": "# MTG: ",
		"description": "議事録（日付を追記）"
	},
	"議事録（日付を追記）5": {
		"prefix": "議事",
		"body": "# MTG: ",
		"description": "議事録（日付を追記）"
	},
}
```

## markdown.json

````
{
	// Place your snippets for markdown here. Each snippet is defined under a snippet name and has a prefix, body and
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"見出し11": {
		"prefix": "見出し",
		"body": "# ",
		"description": "見出し1"
	},
	"見出し21": {
		"prefix": "見出し",
		"body": "## ",
		"description": "見出し2"
	},
	"見出し31": {
		"prefix": "見出し",
		"body": "### ",
		"description": "見出し3"
	},
	"見出し41": {
		"prefix": "見出し",
		"body": "#### ",
		"description": "見出し4"
	},
	"見出し51": {
		"prefix": "見出し",
		"body": "##### ",
		"description": "見出し5"
	},
	"見出し12": {
		"prefix": "み",
		"body": "# ",
		"description": "見出し1"
	},
	"見出し22": {
		"prefix": "み",
		"body": "## ",
		"description": "見出し2"
	},
	"見出し32": {
		"prefix": "み",
		"body": "### ",
		"description": "見出し3"
	},
	"見出し42": {
		"prefix": "み",
		"body": "#### ",
		"description": "見出し4"
	},
	"見出し52": {
		"prefix": "み",
		"body": "##### ",
		"description": "見出し5"
	},
	"リスト1": {
		"prefix": "リスト",
		"body": "- ",
		"description": "リスト"
	},
	"リスト2": {
		"prefix": "リ",
		"body": "- ",
		"description": "リスト"
	},
	"リスト3": {
		"prefix": "list",
		"body": "- ",
		"description": "リスト"
	},
	"リスト4": {
		"prefix": "li",
		"body": "- ",
		"description": "リスト"
	},
	"リスト5": {
		"prefix": "り",
		"body": "- ",
		"description": "リスト"
	},
	"リンク1": {
		"prefix": "リンク",
		"body": "[]()",
		"description": "リンク"
	},
	"リンク2": {
		"prefix": "リ",
		"body": "[]()",
		"description": "リンク"
	},
	"リンク3": {
		"prefix": "link",
		"body": "[]()",
		"description": "リンク"
	},
	"リンク4": {
		"prefix": "li",
		"body": "[]()",
		"description": "リンク"
	},
	"リンク5": {
		"prefix": "り",
		"body": "[]()",
		"description": "リンク"
	},
	"太字1": {
		"prefix": "太字",
		"body": "****",
		"description": "太字"
	},
	"太字2": {
		"prefix": "ふ",
		"body": "****",
		"description": "太字"
	},
	"太字3": {
		"prefix": "bo",
		"body": "****",
		"description": "太字"
	},
	"打消1": {
		"prefix": "打消",
		"body": "~~~~",
		"description": "打ち消し"
	},
	"打消2": {
		"prefix": "打消し",
		"body": "~~~~",
		"description": "打ち消し"
	},
	"打消3": {
		"prefix": "打ち消し",
		"body": "~~~~",
		"description": "打ち消し"
	},
	"打消4": {
		"prefix": "う",
		"body": "~~~~",
		"description": "打ち消し"
	},
	"打消5": {
		"prefix": "strikethrough",
		"body": "~~~~",
		"description": "打ち消し"
	},
	"コード（単行）1": {
		"prefix": "コード",
		"body": "``",
		"description": "コード（単行）"
	},
	"コード（単行）2": {
		"prefix": "コ",
		"body": "``",
		"description": "コード（単行）"
	},
	"コード（単行）3": {
		"prefix": "こ",
		"body": "``",
		"description": "コード（単行）"
	},
	"コード（単行）4": {
		"prefix": "code",
		"body": "``",
		"description": "コード（単行）"
	},
	"コード（単行）5": {
		"prefix": "co",
		"body": "``",
		"description": "コード（単行）"
	},
	"コード（複数）1": {
		"prefix": "コード",
		"body": [
			"```",
			"",
			"```",
		],
		"description": "コード（複数）"
	},
	"コード（複数）2": {
		"prefix": "コ",
		"body": [
			"```",
			"",
			"```",
		],
		"description": "コード（複数）"
	},
	"コード（複数）3": {
		"prefix": "こ",
		"body": [
			"```",
			"",
			"```",
		],
		"description": "コード（複数）"
	},
	"コード（複数）4": {
		"prefix": "code",
		"body": [
			"```",
			"",
			"```",
		],
		"description": "コード（複数）"
	},
	"コード（複数）5": {
		"prefix": "co",
		"body": [
			"```",
			"",
			"```",
		],
		"description": "コード（複数）"
	},
	"引用1": {
		"prefix": "引用",
		"body": "> ",
		"description": "引用"
	},
	"引用2": {
		"prefix": "い",
		"body": "> ",
		"description": "引用"
	},
	"赤色テキスト1": {
		"prefix": "赤色テキスト",
		"body": "<font color=\"Red\"></font>",
		"description": "赤色テキスト"
	},
	"赤色テキスト2": {
		"prefix": "赤",
		"body": "<font color=\"Red\"></font>",
		"description": "赤色テキスト"
	},
	"赤色テキスト3": {
		"prefix": "あか",
		"body": "<font color=\"Red\"></font>",
		"description": "赤色テキスト"
	},
	"赤色テキスト4": {
		"prefix": "あ",
		"body": "<font color=\"Red\"></font>",
		"description": "赤色テキスト"
	},
	"赤色テキスト5": {
		"prefix": "red",
		"body": "<font color=\"Red\"></font>",
		"description": "赤色テキスト"
	},
	"水平線1": {
		"prefix": "水平線",
		"body": "---",
		"description": "水平線"
	},
	"水平線2": {
		"prefix": "す",
		"body": "---",
		"description": "水平線"
	},
	"水平線3": {
		"prefix": "-",
		"body": "---",
		"description": "水平線"
	},
}
````

# vscode 拡張機能

- Git Graph
- GitHub Pull Requests
- AWS Toolkit
- Rainbow CSV
- PowerShell
- deepl

# git init

```
& "C:\Users\TAKAHITO SUZUKI\OneDrive\デスクトップ\dev\start.ps1"
```

> start.ps1

```
Write-Output "------------------"
Write-Output "start"
Write-Output ""

$CurrentDir = Get-Location
echo $CurrentDir

cd $CurrentDir

Write-Output ""
Write-Output "------------------"
Write-Output "git init"
Write-Output ""

git init
git checkout -b master
New-Item a.md
git add a.md
git commit -m 'init'

Write-Output ""
Write-Output "comp"
Write-Output "------------------"
```

# MBTI 診断

- [無料性格診断テスト](https://www.16personalities.com/ja/%E6%80%A7%E6%A0%BC%E8%A8%BA%E6%96%AD%E3%83%86%E3%82%B9%E3%83%88)

# 目標設定シート

## WEBSSO、取り組み

- 基本的な開発を行う。（以下に列挙）
- 分からないことや気になったこと、疑問に感じたことを質問する。
- 限られた時間内で多くの問い合わせやテストを実施し、高品質なサービスを提供する。

## クレカ継続決済

WEBSSO と同じ

## OWASP ZAP

- OWASP ZAP による動的診断をバックグラウンドで実行する（Docker コンテナ）。
- 現在使用している BBSEC 社による脆弱性診断（頂いている診断レポート）と OWASP ZAP による診断結果（作成した診断レポート）を比較する。
- 比較した結果を分析し、説明する。
- 比較した結果、OWASP ZAP による脆弱性診断の有効性が確認できた場合、開発プロセスに組み込めるように準備する（設計や実装、テストなど）。
- テストが OK の場合、リリースし、運用する。

## 担当プロジェクト

- 図や表を多用し、分かりやす資料を作成する。
- 現状仕様や課題管理状況を丁寧かつ分かりやすく説明をし。優先順位を整理する。

## スキルアップ

【目標】AWS の知見を得る
【達成水準】AWS Solution Architect の資格を取得する
【取り組み】

- 試験へ申込みを行い、試験勉強をして、受験する。
- 日頃から AWS に関する情報収集を行う。
- AWS を実際に触ったり、動かすことから知見を蓄える。

## ドキュメント

【目標】
【達成水準】

- システムの仕様を確認するための重要な設計書（機能一覧表やテーブル定義書）が揃っている。
- 設計書が最新である。
- プロダクトを横断して、設計書を確認できる。
- 設計書が簡単に見つかる／確認できる。

【取り組み】

- 先行して設計書を揃える。
- 設計書が簡単に見つかるように、検索ツールを作成する（SharePoint と kendra）
- 使い勝手を工夫する／改善する

## サポート

【目標】
【達成水準】
【取り組み】

- 質問や問い合わせに即レスする。

## 3 年後

【目標】システム設計者として、要件定義の知見を蓄える。迅速かつ効果的に適切な成果物を作成できるようにする。
【達成水準】様々な成果物を作成することが可能となる。
【取り組み】

- 機能一覧やユースケース図の作成
- 権限マトリクス（ステートマシン）の作成
- テーブル関連図（ER 図）の作成
- シーケンス図の作成やコミュニケーション図の作成

## ドキュメント

【目標】
【達成水準】
【取り組み】

# 情報漏洩テスト

## 情報収集

- [Web サーバーのメタファイルに情報漏洩がないか確認する](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/03-Review_Webserver_Metafiles_for_Information_Leakage)
- [Web ページのコンテンツに情報漏洩がないか確認する](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Web_Page_Content_for_Information_Leakage)

## 認証

- [脆弱なパスワードの変更またはリセット機能のテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/09-Testing_for_Weak_Password_Change_or_Reset_Functionalities)
- [暗号化されていないチャネルを介して送信される機密情報のテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/03-Testing_for_Sensitive_Information_Sent_via_Unencrypted_Channels)

- [既定の資格情報のテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials)
  OK

- [脆弱なロックアウトメカニズムのテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/03-Testing_for_Weak_Lock_Out_Mechanism)
  OK

- [認証スキーマをバイパスするためのテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/04-Testing_for_Bypassing_Authentication_Schema)
  テストする

- [脆弱なパスワード記憶のテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/05-Testing_for_Vulnerable_Remember_Password)
  テストする

- [脆弱なパスワードポリシーのテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/07-Testing_for_Weak_Password_Policy)
  OK

- [セッション管理スキーマのテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema)
  余裕があれば、テストする

- [公開セッション変数のテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/04-Testing_for_Exposed_Session_Variables)
  セッションが変わる（ログアウト、セッションタイムアウト）たびに、セッション ID が切り替わることを確認する。

- [ログアウト機能のテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/06-Testing_for_Logout_Functionality)
  シングルサインアウトのテスト：シングルサインオン状態で、IDP 側でサインアウトする。どうなるのが、正しいか？
  → ユーザーサイトは、ログアウト？
  → ユーザーサイトでログイン継続中の場合、ユーザーサイトでログアウト実行後、再認証が実行されるか、検証

- [テストセッションタイムアウト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/07-Testing_Session_Timeout)
  → ログアウトと一緒

- [同時セッションのテスト](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/11-Testing_for_Concurrent_Sessions)
  プライベートブラウジングモードでセッション ID を収集し、最初に生成されたセッション ID で認証に成功するか、テストする
  同じ IP からの複数のセッションでのテスト
  異なる IP からの複数のセッションでのテスト

- []()
- []()
