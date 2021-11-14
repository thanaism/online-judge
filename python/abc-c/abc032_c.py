n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

if 0 in s:
    print(n)
    exit()

from collections import deque

q = deque()
p = 1
ans = 0
for i in range(n):
    q.append(s[i])
    p *= s[i]
    while q and p > k:
        p //= q.popleft()
    ans = max(ans, len(q))
print(ans)
