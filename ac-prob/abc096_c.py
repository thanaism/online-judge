h,w=map(int,input().split())
s=[input() for _ in range(h)]
di=[-1,0,1,0]
dj=[0,1,0,-1]
for i in range(h):
  for j in range(w):
    if s[i][j]=='#':
      count=0
      for k in range(4):
        ni=i+di[k]
        nj=j+dj[k]
        if 0<=ni<h and 0<=nj<w and s[ni][nj]=='#':
          count+=1
      if count==0:
        print('No')
        exit()
print('Yes')