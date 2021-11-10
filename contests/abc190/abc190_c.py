n, m = map(int, input().split())
l = []
for _ in "_" * m:
    l.append([*map(int, input().split())])
k = int(input())
p = []
for _ in "_" * k:
    p.append([*map(int, input().split())])
ans = 0
for i in range(1 << k):
    x = 0
    q = [False] * (n + 1)
    for j in range(k):
        if (i >> j) & 1:
            q[p[j][0]] = True
        else:
            q[p[j][1]] = True
    for h in range(m):
        if q[l[h][0]] and q[l[h][1]]:
            x += 1
    ans = max(ans, x)
print(ans)
