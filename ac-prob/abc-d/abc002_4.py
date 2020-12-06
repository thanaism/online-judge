n,m=map(int,input().split())

p=[-1]*n

def root(x):
    if p[x]<0:return x
    p[x]=root(p[x])
    return p[x]

def union(x,y):
    rx=root(x)
    ry=root(y)
    if rx==ry:return
    if p[rx]<p[ry]:
        rx,ry=ry,rx
    p[rx]+=p[ry]
    p[ry]=rx

def same(x,y):
    if root(x)==root(y):return True
    return False

for _ in range(m):
    x,y=map(int,input().split())
    union(~-x,~-y)

print(min(p)*-1)