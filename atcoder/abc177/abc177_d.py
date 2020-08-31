l=lambda:map(int, input().split())
n,m=l()
p=[-1]*n
def r(x):
  if p[x]<0:return x
  p[x]=r(p[x]);return r(p[x])
def u(x,y):
  x,y=r(x),r(y)
  if x==y: return
  p[x]+=p[y]
  p[y]=x
def e(x,y):
  return r(x)==r(y)
def s(x):
  return -p[r(x)]
for _ in range(m):
  a,b=l()
  u(a-1,b-1)
print(-min(p))