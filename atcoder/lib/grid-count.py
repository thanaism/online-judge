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