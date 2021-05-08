n=int(input())
a=[*map(int,input().split())]
m=min(n,8)
b=[[] for _ in range(200)]
for i in range(1<<m):
    k=0
    ans=[]
    for j in range(m):
        if i>>j&1:
            k+=a[j]
            ans.append(j+1)
    k%=200
    if len(b[k])!=0:
        print('Yes')
        print(len(ans),*ans)
        print(len(b[k]),*b[k])
        exit()
    b[k]=ans
print('No')