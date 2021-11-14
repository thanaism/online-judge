from collections import deque

n = int(input())
a = [*map(int, input().split())]

a.sort()
d = deque(a)
ans = 0
while d:
    _ = d.pop()
    ans += d.pop()
    d.popleft()

print(ans)
