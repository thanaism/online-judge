h, w = map(int, input().split())
s = [input() for _ in range(h)]
MOD = 10 ** 9 + 7

# DP table[0,N)
dp = [[0] * w for _ in range(h)]

# cumsum[0,N+1)
bot = [[0] * (w + 1) for _ in range(h + 1)]
rig = [[0] * (w + 1) for _ in range(h + 1)]
bor = [[0] * (w + 1) for _ in range(h + 1)]

# start position is 1
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        # add cumsum to dp table each dir
        dp[i][j] += bot[i][j] % MOD
        dp[i][j] += rig[i][j] % MOD
        dp[i][j] += bor[i][j] % MOD
        # get MOD
        dp[i][j] %= MOD
        # now can get new cumsum from current new dp
        bot[i + 1][j] += dp[i][j] + bot[i][j]
        rig[i][j + 1] += dp[i][j] + rig[i][j]
        bor[i + 1][j + 1] += dp[i][j] + bor[i][j]
        # reset value at next to wall position
        if s[i][j] == "#":
            dp[i][j] = 0
            bot[i + 1][j] = 0
            rig[i][j + 1] = 0
            bor[i + 1][j + 1] = 0

# output
print(dp[h - 1][w - 1])
