n, m = map(int, input().split())
s = []
for _ in range(m):
    _, *i = map(lambda x: int(x) - 1, input().split())
    b = 0
    for j in i:
        b |= 1 << j
    s.append(b)
p = [*map(int, input().split())]
ans = 0
for i in range(1 << n):
    k = []
    f = True
    for j in s:
        k.append(i & j)
    for l, v in enumerate(k):
        if bin(v).count("1") % 2 != p[l]:
            f = False
    if f:
        ans += 1
print(ans)
