n=int(input())
a=[*map(int,input().split())]
b=[0]*(1<<(n+1))
for i in range(1<<n):
    b[i+(1<<n)]=a[i]
for i in range(n-1,0,-1):
    for j in range(1<<i,1<<(i+1)):
        b[j]=max(b[j*2],b[j*2+1])
c=min(b[2],b[3])
ans=sum([i+1 for i in range(1<<n) if a[i]==c])
print(ans)