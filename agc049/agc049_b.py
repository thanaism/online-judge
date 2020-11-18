"""
n=int(input())
s=[int(l) for l in input()]
t=[int(l) for l in input()]
u=[]
for i,v in enumerate(s):
  if v==1:u.append(i)
u=u[::-1]
cnt=0
for i in range(n):
  if s[i]==1: u.pop()
  if s[i]==t[i]: continue
  if len(u)==0: break
  j=u.pop()
  cnt+=j-i
  s[j]=0
  s[i]=(0 if s[i] else 1)
if s!=t:cnt=-1
print(cnt)
"""
def solve():
  # 入力
  n=int(input())
  s=[int(l) for l in input()]
  t=[int(l) for l in input()]
  # 累積XOR
  xs=[0]
  xt=[0]
  for i in s: xs.append(xs[-1]^i)
  for i in t: xt.append(xt[-1]^i)
  print(xs,xt)
  # S[j]!=S[j+1]となりうる最小のj
  ans=j=0
  for i in range(n+1):
    # iがjを追い越したら更新
    j=max(j,i)
    # 操作不要ならスキップ
    if xs[j]==xt[i]:continue
    # Sが変化しない範囲でインクリメント
    while j<n and xs[j]==xs[j+1]:j+=1
    # 条件を満たすjがなければ不可能
    if j==n:return -1
    # S[j]==T[i]とするためインクリメント
    j+=1
    # 距離が操作回数と等しい
    ans+=j-i
  return ans
# 出力
print(solve())


