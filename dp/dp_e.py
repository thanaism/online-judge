n,w=map(int,input().split())
value=[0]
weight=[0]
for _ in range(n):
  a,b=map(int,input().split())
  weight.append(a)
  value.append(b)

INF=1<<60
dp=[[INF]*100001 for _ in range(n+1)]
dp[0][0]=0 # この境界条件と
for i in range(1,n+1):  # こう取れば場合分けが1つ減る
  for j in range(0,100001):
    if j==0: # この境界条件を考えてなくてバグってた。
      dp[i][j]=0
    if j>=value[i]:
      dp[i][j]=min(dp[i-1][j],dp[i-1][j-value[i]]+weight[i])
    else:
      dp[i][j]=dp[i-1][j]
for i in range(100000,0,-1):
  if w<dp[-1][i]:
    continue
  else:
    print(i)
    break