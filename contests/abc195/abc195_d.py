n,m,q=map(int,input().split())
w,v=[],[]
for i in range(n):
    j,k=map(int,input().split())
    w.append(x)
    v.append(y)
x=[*map(int,input().split())]
for _ in range(q):
    l,r=map(int,input().split())
    run_dp(l,r)
def run_dp(l,r):
    X=x[:l]+x[r+1:] if r<m else x[:l]
    for i in range(n):
        for j in range(len(X)):
            
