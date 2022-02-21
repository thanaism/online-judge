import sequtils, strutils

var n, x: int
(n, x) = stdin.readLine.split.map parseInt
let ab = (0..<n).mapIt(stdin.readLine.split.map parseInt)

var dp = newSeqWith(101, newSeqWith(10001, false))
dp[0][0] = true

for i in 0..<n:
    for j in 0..x:
        let a = ab[i][0]
        let b = ab[i][1]
        if j+a <= x and dp[i][j]:
            dp[i+1][j+a] = true
        if j+b <= x and dp[i][j]:
            dp[i+1][j+b] = true

echo if dp[n][x]: "Yes" else: "No"

