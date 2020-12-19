n=int(input())
a=[*map(int,input().split())]
ans=0
a.sort()
b=[sum(a)]
for i in a:
    b.append(b[-1]-i)
for i in range(1,n+1):
    k=b[i]-a[i-1]*(n-i)
    ans+=k
print(ans)