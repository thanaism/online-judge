n,k=map(int,input().split())
ans=max(0,(n-k+1))
for i in range(1,min(k,n+1)):
    x=i
    cnt=0
    while x<k:
        x*=2
        cnt+=1
    ans+=0.5**cnt
print(ans/n)