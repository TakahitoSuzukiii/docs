# Awesome

- [VSCode(VisualStudioCode)の定番機能を一挙解説](https://qiita.com/midiambear/items/bc0e137ed77153cb421c)

# ワークスペース

- [VS Code のワークスペースをちゃんと使いたい](https://qiita.com/amac-53/items/86b1466e93524844c2a8)

> main.code-workspace

```
{
	"folders": [
		{
			"name": "デスクトップ",
			"path": "C:/Users/TAKAHITO SUZUKI/OneDrive/デスクトップ"
		},
		{
			"name": "ダウンロード",
			"path": "C:/Users/TAKAHITO SUZUKI/Downloads"
		},
		{
			"name": "Dドライブ",
			"path": "D:/"
		},
	],
	"settings": {
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
		}
	}
}
```

# Format

- [Visual Studio Code で保存時自動整形の設定方法](https://qiita.com/mitashun/items/e2f118a9ca7b96b97840)

```
shift + alt + F
```

```
format on
```

# ユーザースニペット

```
    "editor.tabCompletion": "onlySnippets",
    "[markdown]": {
        "editor.quickSuggestions": true,
    }
```

# Todo Tree

- [official](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
- [Octicons（アイコン一覧）](https://primer.style/foundations/icons/)

> setting.json

```
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
```

## Git、Github

- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
