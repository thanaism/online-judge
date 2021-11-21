from collections import defaultdict

n, k = map(int, input().split())

d = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    d[a] += b

now = 0
for i, j in sorted(d.items()):
    now += j
    if now >= k:
        print(i)
        exit()
