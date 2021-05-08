n,k,m,*a=map(int,open(0).read().split())
d=max(m*n-sum(a),0)
print(-1 if d>k else d)