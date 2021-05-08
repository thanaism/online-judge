n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
c=[0]*(n+1)
d=[0]*n
c[0]=min(a[0],b[0])
d[0]=max(b[0]-a[0],0)
for i in range(1,n):
    if d[i-1]>a[i]:
        d[i]=b[i]
        c[i]=a[i]
    else:
        if a[i]-d[i-1]>b[i]:
            c[i]=d[i-1]+b[i]
            d[i]=0
        else:
            c[i]=a[i]
            d[i]=b[i]-a[i]+d[i-1]
c[n]=min(a[n],d[n-1])
print(sum(c))