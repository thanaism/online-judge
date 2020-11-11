n,m=map(int,input().split())
x=sorted([*map(int,input().split())])
if m<=n:
  print(0)
  exit()
dx=sorted([abs(x[i]-x[i-1]) for i in range(1,m)])
print(sum(dx[:m-n]))
