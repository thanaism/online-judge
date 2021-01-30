n,m=map(int,input().split())
l=[]
for _ in range(m):
    l.append([*map(int,input().split())])
k=int(input())
p=[]
for _ in range(k):
    p.append([*map(int,input().split())])
ans=0
for i in range(1<<k):
    s=bin(i)
    s=s[2:].zfill(k)
    x=0
    q=[False]*n
    for j in range(k):
        if s[j]=='0':
            q[p[j][0]-1]=True
        else:
            q[p[j][1]-1]=True
    for h in range(m):
        if q[l[h][0]-1] and q[l[h][1]-1]:
            x+=1
    ans=max(ans,x)
print(ans)
