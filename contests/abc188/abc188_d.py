n, c = map(int, input().split())
a, b, l = [], [], set()
for _ in range(n):
    x, y, z = map(int, input().split())
    a.append((x, z))
    b.append((y, z))
    l |= {x, y + 1}
l = sorted(list(l))
a.sort()
b.sort()
d = dict()
for i, j in a:
    if i in d:
        d[i] += j
    else:
        d[i] = j
for i, j in b:
    if i + 1 in d:
        d[i + 1] -= j
    else:
        d[i + 1] = -j
ans = 0
for i in range(len(l) - 1):
    d[l[i + 1]] += d[l[i]]
    ans += min(c, d[l[i]]) * (l[i + 1] - l[i])
print(ans)
