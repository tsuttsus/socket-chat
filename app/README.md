# チャットアプリ（サンプル）

## クライアント
$ python client.py
テキストを入力して下さい
＞＞＞こんにちは！
サーバーからの回答: こんにちは！お話しすることがありますか？
テキストを入力して下さい
＞＞＞今日の昼ごはんは何が良いと思いますか？あっさりしたものが食べたいです
サーバーからの回答: あっさりとした昼ごはんなら、サラダやスープなどがおすすめです。具体的には、グリーンサラダやミネストローネスープなどが良いでしょう。また、お好み焼きやたこ焼きなどの軽食も良い選択肢です。
テキストを入力して下さい
＞＞＞bye
サーバーからの回答:
クライアント側終了です

## サーバー
$ python server.py
クライアントからの入力待ち状態
接続したクライアント情報:('127.0.0.1', 56489)
クライアントで入力された文字＝こんにちは！
クライアントで入力された文字＝今日の昼ごはんは何が良いと思いますか？あっさりしたものが食べたいです
サーバー側終了です