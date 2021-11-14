n, a = map(int, input().split())
x = [*map(int, input().split())]

m = n * a + 1
dp = [[[0] * m for _ in range(n + 1)] for _ in range(n + 1)]

dp[0][0][0] = 1
for i in range(n):
    for j in range(n):
        for k in range(m):
            dp[i + 1][j][k] += dp[i][j][k]
            if k + x[i] < m:
                dp[i + 1][j + 1][k + x[i]] = dp[i][j][k]

ans = 0
for i in range(1, n + 1):
    ans += dp[n][i][i * a]
print(ans)
