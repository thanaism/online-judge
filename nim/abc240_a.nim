import strutils, sequtils
var a, b: int
(a, b) = stdin.readLine.split.map parseInt
echo if b-a == 1 or (a == 1 and b == 10): "Yes" else: "No"
