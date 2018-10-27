# net_kukai
ネット句会自動化プログラム

前提: PythonとTeXがあると良いが、Pythonだけでもある程度いける。Pythonないときつい

手順  
1. Google formで投句フォームを作る。こんなの  
https://docs.google.com/forms/d/e/1FAIpQLSdn_wIP6wl9uqbITyz3esOsvLtKeF_wVtaRoEugDHG2_UdmuQ/viewform
2. 投句を募る。結果をスプレッドシートからtouku.csvに保存
3. seiki.py を実行。以下が作成される
- seiki_noname.csv: 俳号なし、順番がランダム化された句一覧
- seiki_withname.csv: 上記の俳号あり版。下記選句の自動化に用いる
4. （TeX処理する時のみ）seikitex.pyを実行。以下が作成される
- seiki.tex: 清記TeXファイル
5. （Tex処理する時のみ）seiki.texをコンパイル。以下が作成される
- seiki.pdf: 清記の縦書きpdfファイル  
ただし、ここでは下記藤田眞作氏のホームページから入手できるhaiku.styが必要  
http://xymtex.my.coocan.jp/fujitas2/texlatex/index.html
6. Google formで選句フォームを作る。こんなの  
https://docs.google.com/forms/d/e/1FAIpQLScjxcQ8su--ZyqhIGCooqbhspG2vI-hRFuYtZ5lKcJC3FFWTg/viewform  
7. seiki.pdfをメール送信し、選句を募る。結果をスプレッドシートからsenku.csvに保存
8. senku.py を実行。以下が作成される
- seiki_withpoint_.csv: 俳号あり清記に点数(特選、並選、逆選の数)が追記されたもの。ただし無点句には俳号をつけない
- sen.csv: 俳号・選句・選評・自己紹介
9. （Tex処理する時のみ）senkutex.pyを実行。以下が作成される
- seiki_withpoint.tex: 俳号・点数あり清記TeXファイル
- sen.tex: 選評TeXファイル
10. （Tex処理する時のみ）seiki_withpoint.tex, sen.texをコンパイル。以下が作成される
- seiki_withpoint.pdf: 俳号・点数あり清記pdfファイル(横書き)
- sen.pdf: 選評pdfファイル
11. seiki_withpoint.pdf, sen.pdfをメール送信

TODO
- 機種依存文字を利用可能にする: 直接文字コードを打ってもらえばよいのだが、投句者のコンピュータ能力に依存するので様子見
- ふりがなを利用可能にする: これもちょっと打ってもらえばよいのだが、投句者のコンピュータ能力に依存するので様子見
- 他行形式を利用可能にする: 現状では俳句を上下両端を固定した割り付けでやっているので、他行はすごく間抜けになる。他行の場合のみうまくこなすようなのを、誰か考えてくれ。TeXを使わなければこの問題はおこらないし、上下両端固定をせずただの縦書きにすれば解決する。


