from collections import defaultdict

n, x = map(int, input().split())
l = []
a = []
dp = [defaultdict(int) for _ in range(n + 1)]
dp[0][0] = 1
for _ in range(n):
    i, *j = map(int, input().split())
    l.append(i)
    a.append(list(j))

for j in a[0]:
    dp[1][j] += 1

for i in range(n):
    for j in range(l[i]):
        for k in dp[i]:
            dp[i + 1][k * a[i][j]] += dp[i][k]

print(dp[n][x])
