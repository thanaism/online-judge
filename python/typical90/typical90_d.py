h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append([*map(int, input().split())])
r = [sum(i) for i in a]
c = [0] * w
for j in range(w):
    for i in range(h):
        c[j] += a[i][j]
for i in range(h):
    l = []
    for j in range(w):
        l.append(r[i] + c[j] - a[i][j])
    print(*l)
