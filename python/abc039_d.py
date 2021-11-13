h, w = map(int, input().split())
s = [input() for _ in range(h)]

di = [0, 1, 0, -1] + [1, 1, -1, -1]
dj = [1, 0, -1, 0] + [1, -1, 1, -1]

restore = [["."] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            continue
        ok = True
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if s[ni][nj] != "#":
                ok = False
        if ok:
            restore[i][j] = "#"

replay = [["."] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if restore[i][j] == ".":
            continue
        replay[i][j] = restore[i][j]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            replay[ni][nj] = "#"

for i in range(h):
    replay[i] = "".join(replay[i])

if replay == s:
    print("possible")
    for i in range(h):
        print("".join(restore[i]))
else:
    print("impossible")
