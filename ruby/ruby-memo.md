# PythonistaがRubyを勉強したときのメモ



## 本記事のたてつけ

会社でRubyistの水色コーダーがいらっしゃるため、その人が書くコードを読んだり、個人的に興味のあるコードゴルフを嗜んだりしたいのでPythonistaである私がRubyを始めることにしました。



正直、Pythonistaを名乗れるほどではありませんが、競プロでPythonを使ったり、一時期はPythonでのスクレイピング用プログラム作成をフリーランスとして受託開発したりもしていました。ちなみに機械学習はscikit-learnとか形態要素解析のライブラリをほんのちょびっと触ったことがある程度で、言ってしまえばまったくの専門外です。まだ緑コーダーなので、遅延セグメント木をソラで書けと言われても書けない程度の実装力と思っていただければ間違いないです。



他に使ったことのある言語らしい言語は、Rust、C++、JS/TSとかでしょうか（主に競プロですが）。

使ったことがあるといえるか微妙な言語にHaskellもあります（入門書は読んだレベルといったほうが正しい）。

あと言語と言えるか微妙ですが、dcもある程度はわかります。競プロだとフォーカス外ですがVBAもわかります。他には、JavaもSpring-Bootのスターターをとりあえず動かしたことはあります（つまりJavaまったく分からない）。



ようするにプログラミング初心者です。



## 勉強の仕方

とりあえず、AOJのALDS1を解いていく。ABCのAB問題とITP1はもう他の言語でやってしまったため。

まず自力で解いて、そのあとレートの高い人の回答を見て、知らないメソッドを学んでいく。



## とりあえず気付いたことの羅列



- `{|x| f(x) }`でラムダ式になるっぽい（カーリーブラケットを使う）

- 配列長は`arr.length`

- `tally`とかいう高級な畳み込みがある

- `if Integer === n`みたいにすると整数か判定できる？

  - 型の判定に`===`を使うっぽい（`Float ===`とか`Array ===`とか）

- 整数型への変換は`to_i`（小数型`to_f`、文字列型`to_s`）

- 配列へのプッシュは`push`、ポップは`pop`でそのまま、`append`も使える

- 正規表現リテラルは`/[0-9]+/`みたいに`/`で挟む

  - `/[0-9]+/ =~ str`みたいに比較演算子には`=~`を使うっぽい

- `to_sym`でシンボルに変換する（**シンボルとは……？**）

  - シンボルの[公式ページ](https://docs.ruby-lang.org/ja/latest/class/Symbol.html)
  - シンボルは内部的には整数
  - 文字列と似たように使えるが、文字列と違いimmutable

- `eval`はPythonと同じ感じで使える

- `sort`はin placeじゃない（`sort!`はin place）

- `a <=> b`という演算子があり、結果は`[0, 1, -1]`のいずれかで`a - b`と符号が一致

  - ```ruby
    # こういうオシャレな書き方が可能
    arr = ["==", ">", "<"]
    op = arr[a <=> b]
    ```

- `a <= b <= c`は`b.between?(a,c)`と書ける

- Rubyの代入はPythonと異なり代入した値が返る

- `do ~ end`の`do`は省略可能っぽい

  - `{}`でも代用可能

  - ```ruby
    (1..100).each do |i|
      	# do something
    end
    
    # 以下のようにも書ける
    (1..100).each {|i|
    		# do something
    }
    ```

- `break`はPythonと同じ、`continue`の代わりに`next`を使う

  - `redo`というのもあるらしいが、同じ条件でやり直せる？らしい

- `''`はraw文字列、`""`は`#{var}`を展開してくれる

- スコープは命名で決まる

  - ローカル変数：先頭が英小文字or`_`
  - グローバル変数：先頭が`$`
  - インスタンス変数：先頭が`@`
  - クラス変数：先頭が`@@`
  - 定数：先頭が英大文字
  - メソッド名はスネークケース
  - クラス名、モジュール名はアッパーキャメル？

- Rubyでは`false`と`nil`のみが偽（`0`は真となる）

- インデントはスペース2つが慣習！

- 小数の桁数指定は`"%.5f" % float_val`もしくは`sprintf("%.5f", float_val)`

- πは`Math::PI`で使える

  - `include Math`しておくと`PI`だけで使える
  - [あんまり衝突しそうな名前はない](https://docs.ruby-lang.org/ja/latest/class/Math.html)ので競プロではためらわず`include`しちゃってよさそう

- `send`メソッドを使って`eval`みたいなことができる

  - `3.send(:+,5) #=> 8`

  - ```ruby
    a = 3
    b = 5
    op = "+"
    puts a.send(op,b) #=> 8
    
    # sendはレシーバの持つメソッドを呼び出す
    class User
      def age(num)
        puts "I'm #{num} years old."
      end
    end
    user = User.new
    user.age(20)          #=> I'm 20 years old.
    user.send("age", 20)  #=> I'm 20 years old.
    user.send(:age, 20)   #=> I'm 20 years old.
    ```

- 速度面を考えると`arr.sum`を使うべきで、`arr.inject(:+)`は遅く、`arr.inject(&:+)`はもっと遅い

- `gets.split(" ").map(&:to_i)`とかの中にある`&`は、`to_proc`メソッドを呼び出す

  - 具体的には`Symbol#to_proc`メソッド

  - 以下のようなシンタックスシュガーと思ってればいいっぽい

  - ```ruby
    ["a", "b"].map(&:upcase) #=> ["A", "B"]
    
    ["a", "b"].map do |str|
      :upcase.to_proc.call(str)
    end
    #=> ["A", "B"]
    ```

- `?a`のように長さ1の文字列は`?`でリテラルとして表記可能

- `#=>`は慣用的に実行結果を表すために使う

- `ClassName#method_name`ドキュメント内でどのクラスのインスタンスメソッドかを示す書き方

- [%記法](https://docs.ruby-lang.org/ja/latest/doc/spec=2fliteral.html#percent)はコードゴルフに使えそうなのでぜひ覚えておく

- `*`はスプラット演算子と呼ぶ

  - `a, *b = gets.split(" ")`みたいな感じ、Pythonとだいたい同じはず

- ハッシュの書き方にいくつかあるっぽい？

  - `{ a:"aaa", b:"bbb" }`
  - `{ :a => "aaa", :b => "bbb" }`

- Rangeの`..`と`...`がある

  - Rustをやっているとわかりにくい
  - Rustの`..=`はRubyの`..`で、Rustの`..`がRubyの`...`

- JSのスプレッド構文に似たやつがある

  - ```ruby
    # 受け取った引数をそのまま別のメソッドに渡せる
    def foo(...)
      bar(...)
    end
    ```

- `->`は新しいlamba記法

  - ```ruby
    # どちらで書いても同じ
    ->(a,b){f(a,b)}
    lambda{|a, b| f(a, b)}
    ```

- 埋め込みドキュメント

  - ```ruby
    =begin
    ここには複数行の
    埋め込みドキュメントを
    記載できます
    =end
    ```

- Rustと同じく数値リテラルに`_`を含むことが可能（`1000_000_007`など）

- 番号指定パラメータとかいうコードゴルフのためにあるような機能があるっぽい

  - ```ruby
    # 同じ意味
    (1..10).map {|n| n * 2 }
    (1..10).map { _1 * 2 }
    
    [3, 1, 2].sort {|n, m| m <=> n }
    [3, 1, 2].sort { _2 <=> _1 }
    ```

- `;`で改行と同じ扱い

- ブロックローカル変数にも`;`を使う

  - `[1,2,3].each{|v; z| z = v * 2 ... }`

- `Comparable#clamp`というメソッドがある

  - ```ruby
    12.clamp(0, 100)  #=> 12
    530.clamp(0, 100) #=> 100
    ```

- 組み込みライブラリの`Enumerable`に含まれる[メソッド](https://docs.ruby-lang.org/ja/latest/class/Enumerable.html)は事前に覚えておいたほうがよさそう

## Integerクラス

- `a%b`の結果の符号は`b`に一致するっぽい
- 数値に対して`16[4] #=> 1`とかやるとビットが立ってるか検査できる（ウケる）
- `allbits?`、`anybits?`、`nobits?`というビットの数を検査するメソッドあり
- `bit_length`もある
- `65.chr #=> "A"`のように番号から文字列に直す
- `digits`で基数を指定して各位を配列に格納
- `divmod`で商と剰余の配列を得る、`modulo`と`remainder`もある
- `fdiv`により小数で除算の結果を得る
- `even?`と`odd?`があるが、`a&1==1`とかより遅いらしい
- `gcd`と`lcm`は組み込みで存在する、`gcdlcm`という配列で両方受け取るのもある
- `to_s`と`inspect`は基数を指定して数値を文字列に
- `next`と`succ`があるが、`+= 1`でいいと思う（`pred`もある）
- `ord`は書き方は違うが、Pythonと使い方は同じ
- `rationalize`で有理数に変換する
- `n.truncate(-3)`などとすると下3桁が`0`で`n`に最も近い整数が返る

## Enumerableクラス

- `all?`と`any?`はブロックやパターンを伴うことができる
  - `all? {|item| ... } -> bool`
  - `all? {/pattern/} -> bool`
- `chain`で複数のイテレータをつなげる
- `chunk {|elt| ... }`でブロックの評価ごとのチャンクに分割する、チャンクに評価値を含む
- `chunk_while {|elt_before, elt_after| ... }`は引数を2つ取り、ブロックの評価が偽で分かれる
- `map` = `collect`
- `flat_map` = `collect_concat`
- `cycle`で無限回繰り返し、`cycle(n)`も可
- `find` = `detect`はブロックのみを取る
- `drop(n)`は先頭`n`個を捨てる
  - `drop_while`はブロックの評価が継続するところまで捨てる
- `each_cons(n)`は重複ありで`n`個ずつにする`(1..10) #=> [1,2,3], [2,3,4], [3,4,5]`
- `each_entry`は`forEach`的な感じ
- 

