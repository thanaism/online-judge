n=int(input())
l=[]
d=[]
for _ in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
    d.append(b-a)
m=sum(d)
ds=[]
dg=[]
for i in range(n):
    s=0
    g=0
    for j  in range(n):
        a,b=l[i]
        c,d=l[j]
        s+=abs(a-c)
        g+=abs(b-d)
    ds.append(s)
    dg.append(g)
print(min(ds)+min(dg)+m)