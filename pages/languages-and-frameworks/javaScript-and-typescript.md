## Awesome
- [Awesome JavaScript](https://github.com/sorrycc/awesome-javascript#awesome-javascript- "Awesome JavaScript")
- [Awesome TypeScript](https://github.com/dzharii/awesome-typescript#awesome-typescript "Awesome TypeScript")
- [Awesome TypeScript2](https://github.com/semlinker/awesome-typescript "Awesome TypeScript2")
## Roadmap
- [Roadmap JavaScript](https://roadmap.sh/javascript)
- [Roadmap TypeScript](https://roadmap.sh/typescript)
## JavaScript
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [文書の操作](https://developer.mozilla.org/ja/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents#%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%83%A2%E3%83%87%E3%83%AB)
> Window
> ウィンドウはウェブページが読み込まれる部分の回りのブラウザーの枠です。これは JavaScript では Window オブジェクトで表わされます。このオブジェクトに備わるメソッドを使って、ウィンドウの大きさを調べたり（Window.innerWidth と Window.innerHeight を参照）、ウィンドウに読み込まれる文書を操作したり、その文書に関係するデータをクライアント側で保存したり（例えばローカルデータベースや他のデータ保存機構）、現在のウィンドウに対してイベントハンドラーを追加したりすることができます。
> Navigator
> ナビゲーターは、ブラウザーの状態やウェブで使われているようなブラウザーの身元（つまりユーザーエージェント）を表わします。JavaScript では Navigator オブジェクトで表わされます。このオブジェクトを使用して、ユーザーの好む言語や、ユーザーのウェブカメラからのメディアストリームなどを取得することができます。
> Dom
> 文書化（ブラウザーでは DOM で表される）は、ウィンドウに読み込まれた実際のページであり、JavaScript では Document オブジェクトで表されます。このオブジェクトを使用して、文書を構成する HTML と CSS に関する情報を返したり操作したりすることができます。例えば、DOM 内の要素への参照を取得し、そのテキストコンテンツを変更し、新しいスタイルを適用し、新しい要素を作成して現在の要素に子として追加したり、あるいは完全に削除したりすることができます。
> Node
> ツリーのそれぞれの項目は、ノードと呼ばれます。上の図では、ノードには要素（HTML、HEAD、META などと識別される）を表すものや 、テキスト（#text と識別される）を表すものがあることが分かります。他の種類のノードもありますが、よく見かけるものはこれらのものです。
- [非同期 JavaScript](https://developer.mozilla.org/ja/docs/Learn/JavaScript/Asynchronous)
- [プロミスの使い方](https://developer.mozilla.org/ja/docs/Learn/JavaScript/Asynchronous/Promises)
> プロミスチェーン、複数のプロミスの組み合わせ
```
Promise.all([...Array])
Promise.any([...Array])
async await
```
- [Client-side_JavaScript_frameworks](https://developer.mozilla.org/ja/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks)
- [Thread (スレッド)](https://developer.mozilla.org/ja/docs/Glossary/Thread)
- [ワーカー入門](https://developer.mozilla.org/ja/docs/Learn/JavaScript/Asynchronous/Introducing_workers)
> スレッドとは、プログラムが従う一連の命令です。
> マルチスレッドコードでは、自分のスレッドがいつ中断され、他のスレッドが実行する機会を得るかわかりません。そのため、両方のスレッドが同じ変数にアクセスすると、いつ変数が予期せぬ変化を起こすか分からず、見つけにくいバグが発生する可能性があるのです。
> 専用ワーカー：単一のスクリプトインスタンスで使用されることを意味しています。
> 共有ワーカー：異なるウィンドウで動作する複数の異なるスクリプトで共有することができます。
> サービスワーカー：プロキシサーバーのような役割を果たし、リソースをキャッシュすることで、ユーザーがオフラインのときでもウェブアプリケーションを動作させることができます。プログレッシブウェブアプリの重要な構成要素である。
- [サービスワーカーAPI](https://developer.mozilla.org/ja/docs/Web/API/Service_Worker_API)
- [サービスワーカーの使用](https://developer.mozilla.org/ja/docs/Web/API/Service_Worker_API/Using_Service_Workers)
### PUSH通知
> サーバーからクライアントに対してプッシュ通知メッセージを送信するための仕組み。ブラウザが閉じている場合でも、サーバーからの通知をユーザーにプッシュする機能
- [プッシュ API](https://developer.mozilla.org/ja/docs/Web/API/Push_API)
- [ウェブプッシュ API 通知のベストプラクティス](https://developer.mozilla.org/ja/docs/Web/API/Push_API/Best_Practices)
### 通知
> ブラウザ内でのユーザーに対する通知。バックグラウンドでの通知されない
- [通知 API](https://developer.mozilla.org/ja/docs/Web/API/Notifications_API)
- [通知 API の使用](https://developer.mozilla.org/ja/docs/Web/API/Notifications_API/Using_the_Notifications_API)
- [ウェブアプリマニフェスト](https://developer.mozilla.org/ja/docs/Web/Manifest)
### PWA
- [プログレッシブウェブアプリ (PWA)](https://developer.mozilla.org/ja/docs/Web/Progressive_web_apps)
- [PWA](https://web.dev/progressive-web-apps)
- [Debugging PWA](https://developer.chrome.com/blog/devtools-tips-18/)
- [サーバサイド Web サイトプログラミング](https://developer.mozilla.org/ja/docs/Learn/Server-side)
## Typescript
- [docs](https://www.typescriptlang.org/ja/docs "docs")
- [サバイバルTypescript](https://typescriptbook.jp "サバイバルTypescript")
- [TypeScriptの学習リソース](https://typescriptbook.jp/learning-resources#%E6%A7%8B%E6%88%90%E8%A6%81%E7%B4%A0 "TypeScriptの学習リソース")
- [roadmap](https://roadmap.sh/typescript "roadmap")
- [索引:記号とキーワード](https://typescriptbook.jp/symbols-and-keywords "索引:記号とキーワード")
- [判別可能なユニオン型](https://typescriptbook.jp/reference/values-types-variables/discriminated-union "判別可能なユニオン型")
- [インターセクション型](https://typescriptbook.jp/reference/values-types-variables/intersection "インターセクション型")
- [型ガード](https://typescript-jp.gitbook.io/deep-dive/type-system/typeguard "型ガード")
- [公称型と構造的部分型](https://typescriptbook.jp/reference/values-types-variables/structural-subtyping "公称型と構造的部分型")
- [Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html "Generics")
- [Keyof](https://www.typescriptlang.org/docs/handbook/2/keyof-types.html "Keyof")
- [Typeof](https://www.typescriptlang.org/docs/handbook/2/typeof-types.html "Typeof")
- [Indexed Access Types](https://www.typescriptlang.org/docs/handbook/2/indexed-access-types.html "Indexed Access Types")
- [Conditional Types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html "Conditional Types")
- [Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html "Mapped Types")
- [Template Literal Types](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html "Template Literal Types")