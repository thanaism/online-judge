"""n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

# Union-Find
p=[-1]*n
def root(x):
  if p[x]<0:return x
  p[x]=root(p[x]);return p[x]
def union(x,y):
  x,y=root(x),root(y)
  if x==y: return
  if size(x)<size(y):
    x,y=y,x
  # p[x]+=p[y]
  p[y]=x
def same(x,y):
  return root(x)==root(y)
def size(x):
  return -p[root(x)]
def roots():
  return [i for i,x in enumerate(p) if x<0]
def members(x):
  r=root(x)
  return [i for i in range(n) if root(i)==r]
for _ in range(m):
  ci,di=map(int,input().split())
  union(ci-1,di-1)

sum_a,sum_b=[0]*n,[0]*n
for i in range(n):
  ri=root(i)
  sum_a[ri]+=a[i]
  sum_b[ri]+=b[i]

for i,j in zip(sum_a,sum_b):
  if i!=j:
    print('No');exit()
print('Yes')

# for i in roots():
#   sum_a=sum_b=0
#   for j in members(i):
#     sum_a+=a[j]
#     sum_b+=b[j]
#   if sum_a!=sum_b:
#     print('No');exit()
# print('Yes')"""

f = lambda: map(int, input().split())
n, m = f()
a = [*f()]
b = [*f()]
# Union-Find
p = [-1] * n


def root(x):
    if p[x] < 0:
        return x
    p[x] = root(p[x])
    return p[x]


def union(x, y):
    rx, ry = root(x), root(y)
    if rx == ry:
        return
    p[ry] = rx


for _ in range(m):
    c, d = f()
    union(c - 1, d - 1)
sum_a, sum_b = [0] * n, [0] * n
for i in range(n):
    ri = root(i)
    sum_a[ri] += a[i]
    sum_b[ri] += b[i]
if sum_a == sum_b:
    print("Yes")
else:
    print("No")
