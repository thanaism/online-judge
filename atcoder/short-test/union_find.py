p=[-1]*n
def root(x):
  if p[x]<0:return x
  p[x]=root(p[x]);return p[x]
def union(x,y):
  x,y=root(x),root(y)
  if x==y: return
  p[x]+=p[y]
  p[y]=x
def same(x,y):
  return root(x)==root(y)
def size(x):
  return -p[r(x)]