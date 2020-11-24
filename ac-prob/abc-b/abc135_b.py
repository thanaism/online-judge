n,*p=map(int,open(0).read().split())
q=sorted(p)
ans='NO'
for i in range(n-1):
    for j in range(i,n):
        r=p.copy()
        r[i],r[j]=r[j],r[i]
        if q==r:ans='YES'
print(ans)