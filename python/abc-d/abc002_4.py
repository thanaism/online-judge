n,m=map(int,input().split())
r=set()
for _ in range(m):
    x,y=map(int,input().split())
    r|={(x-1,y-1)}
ans=0
for i in range(1<<n):
    b=bin(i)[2::].zfill(n)
    ok=True
    for j in range(n):
        for k in range(j+1,n):
            if b[j]==b[k]=='1':
                if (j,k) not in r:
                    ok=False
                    break
    if ok:ans=max(b.count('1'),ans)
print(ans)