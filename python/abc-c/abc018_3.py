h, w, x = map(int, input().split())
a = [input() for _ in range(h)]

u = [[0] * w for _ in range(h)]
d = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        for k in range(h):
            if i + k >= h:
                break
            if a[i + k][j] == "o":
                u[i][j] += 1
            else:
                break
        for k in range(h):
            if i - k < 0:
                break
            if a[i - k][j] == "o":
                d[i][j] += 1
            else:
                break

ans = 0
for i in range(h):
    for j in range(w):
        ok = True
        for k in range(x):
            if j + k >= w or j - k < 0:
                ok = False
                break
            if (
                u[i][j + k] < x - k
                or d[i][j + k] < x - k
                or u[i][j - k] < x - k
                or d[i][j - k] < x - k
            ):
                ok = False
        if ok:
            ans += 1
print(ans)
