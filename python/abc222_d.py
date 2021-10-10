n = int(input())
a = [*map(int,input().split())]
b = [*map(int,input().split())]
MOD = 998244353

dp = [[0]*3300 for _ in range(3300)]
for i in range(3001): dp[0][i] = 1

for i in range(1,n+1):
	for j in range(a[i-1],b[i-1]+1):
		dp[i][j] += dp[i-1][j]
		dp[i][j] %= MOD
	for j in range(1,3001):
		dp[i][j] += dp[i][j-1]
		dp[i][j] %= MOD
print(dp[n][b[-1]])