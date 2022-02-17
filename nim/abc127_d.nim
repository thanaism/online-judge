import sequtils, strutils, tables, algorithm

var n,m: int
(n,m) = stdin.readLine.split.map parseInt
let a = stdin.readLine.split.map parseInt
let bc = (0..<m).mapIt(stdin.readLine.split.map parseInt)

var t = toCountTable(a)
for i in bc: t.inc(i[1], i[0])

var ans: int = 0
for i in toSeq(t.pairs).sorted.reversed:
    ans += i[0] * min(i[1], n)
    n = max(n - i[1], 0)
    if n == 0: break

echo ans
