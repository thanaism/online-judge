n, m = map(int, input().split())
edges = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a][b] = True
    edges[b][a] = True

from itertools import permutations

ans = 0
for p in permutations(range(2, n + 1), n - 1):
    p = (1,) + p
    ok = True
    for i in range(1, n):
        a, b = p[i], p[i - 1]
        if not edges[a][b]:
            ok = False
            break
    if ok:
        ans += 1

print(ans)
