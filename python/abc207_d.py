n = int(input())
a, b = [], []
for _ in range(n):
    i, j = map(int, input().split())
    a.append(i)
    b.append(j)

c, d = [], []
for _ in range(n):
    i, j = map(int, input().split())
    c.append(i)
    d.append(j)


def dist(a, b, c, d):
    dx = a - c
    dy = b - d
    return dx * dx + dy * dy


def outer_product(a, b, c, d, e, f):
    return (a - e) * (d - f) - (b - f) * (c - e)


if n == 1:
    print("Yes")
    exit()

if n == 2:
    if dist(a[0], b[0], a[1], b[1]) == dist(c[0], d[0], c[1], d[1]):
        print("Yes")
        exit()
    else:
        print("No")
        exit()

ds = [[0] * 3 for _ in range(n)]
for i in range(n):
    ds[i][0] = dist(a[0], b[0], a[i], b[i])
    ds[i][1] = dist(a[1], b[1], a[i], b[i])
    ds[i][2] = outer_product(a[0], b[0], a[1], b[1], a[i], b[i])
ds.sort()

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dt = [[0] * 3 for _ in range(n)]
        for k in range(n):
            dt[k][0] = dist(c[i], d[i], c[k], d[k])
            dt[k][1] = dist(c[j], d[j], c[k], d[k])
            dt[k][2] = outer_product(c[i], d[i], c[j], d[j], c[k], d[k])
        dt.sort()
        if dt == ds:
            print("Yes")
            exit()

print("No")
