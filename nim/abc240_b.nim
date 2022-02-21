import sequtils, strutils, tables
var _ = stdin.readLine.parseInt
let a = stdin.readLine.split.map parseInt

echo a.toCountTable.len
