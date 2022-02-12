h, w, K = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(h)]

b = sum(a, [])

INF = 1 << 60
dp = [[[INF] * (K + 1) for _ in range(w)] for _ in range(h)]
ans = INF

for x in b:
    for i in range(h):
        for j in range(w):
            for k in range(K + 1):
                dp[i][j][k] = INF
    if a[0][0] >= x:
        dp[0][0][1] = a[0][0]
    if a[0][0] <= x:
        dp[0][0][0] = 0
    for i in range(h):
        for j in range(w):
            for k in range(K + 1):
                if i != 0:
                    if a[i][j] >= x and k != K:
                        dp[i][j][k + 1] = min(
                            dp[i][j][k + 1], dp[i - 1][j][k] + a[i][j]
                        )
                    if a[i][j] <= x:
                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                if j != 0:
                    if a[i][j] >= x and k != K:
                        dp[i][j][k + 1] = min(
                            dp[i][j][k + 1], dp[i][j - 1][k] + a[i][j]
                        )
                    if a[i][j] <= x:
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j - 1][k])
    ans = min(ans, dp[h - 1][w - 1][K])

print(ans)
