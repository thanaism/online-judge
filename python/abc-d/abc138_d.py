from collections import defaultdict, deque

n, q = map(int, input().split())

edges = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

dp = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    dp[p] += x

used = [0] * n
used[0] = 1
d = deque()
d.append(0)
while d:
    i = d.popleft()
    for j in edges[i]:
        if used[j]:
            continue
        dp[j] += dp[i]
        d.append(j)
        used[j] = 1

print(*dp)
