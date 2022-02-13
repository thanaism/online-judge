from collections import Counter

n, q = map(int, input().split())
a = list(map(int, input().split()))
xk = [list(map(int, input().split())) for _ in range(q)]

map = Counter()
ans = {}

for i in range(n):
    map[a[i]] += 1
    ans[(a[i], map[a[i]])] = i + 1

for x, k in xk:
    if (x, k) in ans:
        print(ans[(x, k)])
    else:
        print(-1)
