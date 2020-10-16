"""ちょっと実装としてはセンスなさめ
h,w=map(int,input().split())

s=[]
for _ in range(h):
  s+=list(input()),

for i in range(h):
  for j in range(w):
    if s[i][j]=='.':
      count=0
      if i!=0:
        if s[i-1][j]=='#':
          count+=1
        if j!=0 and s[i-1][j-1]=='#':
          count+=1
        if j!=w-1 and s[i-1][j+1]=='#':
          count+=1
      if j!=0 and s[i][j-1]=='#':
          count+=1
      if j!=w-1 and s[i][j+1]=='#':
          count+=1
      if i!=h-1:
        if j!=0 and s[i+1][j-1]=='#':
            count+=1
        if s[i+1][j]=='#':
            count+=1
        if j!=w-1 and s[i+1][j+1]=='#':
            count+=1
      s[i][j]=str(count)

for l in s:
  print(''.join(l))
"""

h,w=map(int,input().split())
s=[[*input()] for _ in range(h)]
di=[-1,-1,-1,0,0,1,1,1]
dj=[-1,0,1,-1,1,-1,0,1]
for i in range(h):
  for j in range(w):
    if s[i][j]=='#':continue
    count=0
    for k in range(8):
      ni=i+di[k]
      nj=j+dj[k]
      if ni<0 or ni>h-1:continue
      if nj<0 or nj>w-1:continue
      if s[ni][nj]=="#":count+=1
    s[i][j]=str(count)
  print(''.join(s[i]))