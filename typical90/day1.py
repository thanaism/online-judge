n,l=map(int,input().split())
k=int(input())
a=[0]+[*map(int,input().split())]+[l]
d=[a[i+1]-a[i] for i in range(n+1)]
e=[[v,i] for i,v in enumerate(d)]
b=sorted(e)
print(b)
c=b[n-k-1][0]
print(c)
ans=l
m=l
for i in range(len(e)):
    if e[i][0]<=c:
        if i<len(e)-1:
            e[i+1][0]+=e[i][0]
            m=min(e[i+1][0],m)
        else:
            e[i-1][0]+e[i][0]
print(m)