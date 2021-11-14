n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]

from collections import defaultdict

indegrees = defaultdict(int)
endpoints = defaultdict(set)
for a, b in ab:
    if b not in endpoints[a]:
        indegrees[b] += 1
    endpoints[a].add(b)

from heapq import *

q = []
for i in range(n):
    if indegrees[i + 1] == 0:
        heappush(q, i + 1)

ans = []
while q:
    i = heappop(q)
    ans.append(i)
    for j in endpoints[i]:
        indegrees[j] -= 1
        if indegrees[j] == 0:
            heappush(q, j)

if len(ans) < n:
    print(-1)
else:
    print(*ans)
