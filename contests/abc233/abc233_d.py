from collections import Counter

n, k = map(int, input().split())
a = [0] + [*map(int, input().split())]
for i in range(1, n + 1):
    a[i] += a[i - 1]
d = Counter(a)
ans = 0
for i in a:
    d[i] -= 1
    ans += d[i + k]
print(ans)
