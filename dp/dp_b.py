n,k=map(int,input().split())
*h,=map(int,input().split())
INF=1<<60
dp=[INF]*n
dp[0]=0
for i in range(n):
  for j in range(k+1):
    if i>=j:
      dp[i]=min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
print(dp[-1])