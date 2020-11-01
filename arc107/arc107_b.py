n,k=map(int,input().split())
res=0
for i in range(2,2*n+1):
  if 2<=i-k<=2*n:
    x,y=i-1,i-k-1
    res+=(x if x<=n else x-(x-n)*2)*(y if y<=n else y-(y-n)*2)
print(res)