n,k=map(int,input().split())
a=[]
for _ in range(n):
  a.append(list(map(int,input().split())))

class UFT:
  def __init__(self,n):
    self.p=[-1]*n
  def root(self,x):
    if self.p[x]<0: return x
    self.p[x]=self.root(self.p[x])
    return self.p[x]
  def union(self,x,y):
    rx=self.root(x)
    ry=self.root(y)
    if rx==ry: return
    if self.size(rx)>self.size(ry):
      rx,ry=ry,rx
    self.p[rx]+=self.p[ry]
    self.p[ry]=rx
  def size(self,x):
    return -self.p[x]
  def sizes(self):
    return [self.size(i) for i,v in enumerate(self.p) if v<0]

row=UFT(n)
col=UFT(n)
for i in range(n):
  for j in range(n):
    row_flg=True
    col_flg=True
    for m in range(n):
      if a[i][m]+a[j][m]>k:
        row_flg=False
      if a[m][i]+a[m][j]>k:
        col_flg=False
    if row_flg:
      row.union(i,j)
    if col_flg:
      col.union(i,j)

from math import factorial
row_res=1
for i in row.sizes():
  row_res*=factorial(i)%998244353
col_res=1
for i in col.sizes():
  col_res*=factorial(i)%998244353

print(row_res*col_res%998244353)