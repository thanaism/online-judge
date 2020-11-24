n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
c=[*map(int,input().split())]
ans=0
for i in range(n):
    ans+=b[a[i]-1]
    if i>0 and a[i-1]==a[i]-1:ans+=c[a[i-1]-1]
print(ans)