import sequtils, strutils

let n = stdin.readLine.parseInt
let a = stdin.readLine.split.map parseInt

var cyl: seq[seq[int]] = @[]
var now = 0
var cmb = 0

for i in 0..<n:
    now += 1
    if cyl.len != 0 and cyl[^1][0] == a[i]:
        cmb += 1
        discard cyl.pop
        if cmb == a[i]:
            now -= cmb
            if cyl.len != 0:
                cmb = cyl[^1][1]
            else:
                cmb = 0
        else:
            cyl.add(@[a[i], cmb])
    else:
        cmb = 1
        cyl.add(@[a[i], cmb])
    echo now
