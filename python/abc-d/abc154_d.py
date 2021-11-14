n, k = map(int, input().split())
p = [*map(int, input().split())]

t = [0] + [(i + 1) * i // 2 / i for i in p]

for i in range(1, n + 1):
    t[i] += t[i - 1]

ans = 0
for i in range(n + 1):
    if i + k < n + 1:
        point = t[i + k] - t[i]
        ans = max(ans, point)

print(ans)
