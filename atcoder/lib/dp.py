
n=4
W=5
v=(3,2,4,2)
w=(2,1,3,2)
def dp(i,j):
  if i==n:
    # exhausted
    res=0
  elif w[i]>j:
    # weight over
    res=dp(i+1,j)
  else:
    res=max(dp(i+1,j),dp(i+1,j-w[i])+v[i])
  return res

memo=[[None]*(10**5+1) for _ in range(n+1)]
# print(memo)
def memo_dp(i,j):
  if memo[i][j] is not None:
    return memo[i][j]
  if i==n:
    # exhausted
    res=0
  elif w[i]>j:
    # weight over
    res=memo_dp(i+1,j)
  else:
    res=max(memo_dp(i+1,j),memo_dp(i+1,j-w[i])+v[i])
  return res

print(memo_dp(0,W))