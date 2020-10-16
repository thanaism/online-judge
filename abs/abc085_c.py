n,y=map(int,input().split())
l=[-1]*3
for i in range(n+1):
 for j in range(n-i+1):
  if 9*i+4*j+n==y/1000:l=i,j,n-i-j
print(*l)