MOD = 10 ** 9 + 7
h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(input())
dp = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(h):
    for j in range(w):
        if i == j == 0:
            dp[i][j] = 1
            continue
        if grid[i][j] == "#":
            dp[i][j] = 0
            continue
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
print(dp[h - 1][w - 1] % MOD)
