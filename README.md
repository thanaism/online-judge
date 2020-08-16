# atcoder-python
自分用の勉強メモ

## 剰余の性質
漸化式で表されるような項に対しては剰余の周期性を利用すること（@abc174)
Pを法とするような剰余は高々P通りしかないということにも着目すること
### 交換法則・結合法則
- $ a \equiv b \Leftrightarrow ac \equiv bc \pmod P $
- $ a \equiv b \Leftrightarrow a+c \equiv b+c \pmod P $
- $ a \equiv b \Leftrightarrow a-c \equiv b-c \pmod P $

### 群と逆元
剰余は群を作る？ため、群論から言えば任意の元に対する逆元が存在する
これについては、まだ必要な問題に当たっていないため後回し

## Python itertools
繰り返しや全列挙系のメソッドがまとまっているライブラリ
実行速度の検証していないが、B問題くらいまでは超簡潔に記述できそう。