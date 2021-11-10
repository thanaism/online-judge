n, m = map(int, input().split())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = i
for j in range(m + 1):
    dp[0][j] = j
for i in range(n):
    for j in range(m):
        dp[i + 1][j + 1] = (
            min(dp[i + 1][j], dp[i][j + 1], dp[i][j] - (a[i] == b[j])) + 1
        )
print(dp[n][m])
