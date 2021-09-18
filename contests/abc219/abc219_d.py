n=int(input())
x,y=map(int,input().split())
l=[tuple(map(int,input().split())) for _ in range(n)]
INF=1<<60
dp=[[[INF]*(330) for _ in range(330)] for _ in range(330)]
dp[0][0][0]=0
for i in range(n):
	a,b=l[i]
	for j in range(x+1):
		for k in range(y+1):
			dp[i+1][min(j+a,x)][min(k+b,y)] = min(
				dp[i+1][min(j+a,x)][min(k+b,y)],
				dp[i][min(j,x)][min(k,y)]+1
				)
			dp[i+1][j][k] = min(
				dp[i+1][j][k],
				dp[i][j][k]
			)
ans = dp[n][x][y]
if ans==INF: ans=-1
print(ans)
