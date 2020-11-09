n=int(input())
x,y=[],[]
for _ in range(n):
  ix,iy=map(int,input().split())
  x.append(ix)
  y.append(iy)
ans=0
for i in range(n):
  for j in range(i+1,n):
    dx=x[i]-x[j]
    dy=y[i]-y[j]
    ans=max(ans,dx*dx+dy*dy)
print(ans**0.5)