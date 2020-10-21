n,w=map(int,input().split())
# dpテーブルの要件を意識して添字バグを防ぐこと
# なにも選択しない => 0で初期化
value=[0]
weight=[0]
for _ in range(n):
  a,b=map(int,input().split())
  weight.append(a)
  value.append(b)

# [0-N]x[0-W]のDPテーブルとなる
dp=[[0]*(w+1) for _ in range(n+1)]

for i in range(1,n+1):  # こう取れば場合分けが1つ減る
  for j in range(1,w+1):
    if j>=weight[i]:
      dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
    else:
      dp[i][j]=dp[i-1][j]
print(dp[-1][-1])