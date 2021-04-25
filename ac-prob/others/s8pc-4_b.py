n,k=map(int,input().split())
a=[*map(int,input().split())]
ans=1<<60
for i in range(1<<n):
    x=h=c=0
    b=a.copy()
    for j in range(n):
        if (i>>j)&1:
            if b[j]<=h:
                x+=h-b[j]+1
                b[j]=h+1
        if h<b[j]:
            c+=1
        h=max(h,b[j])
    if c>=k:
        ans=min(ans,x)
print(ans)
                                                   