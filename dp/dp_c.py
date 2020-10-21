n=int(input())
action=[]
for _ in range(n):
  action.append([*map(int,input().split())])
dp=[[0]*3 for _ in range(n)]
for i in range(3):
  dp[0][i]=action[0][i]
for i in range(n):
  if i>0:
    for j in range(3):
      for k in range(3):
        if j!=k:
          dp[i][j]=max(dp[i][j],dp[i-1][k]+action[i][j])
print(max(dp[-1]))