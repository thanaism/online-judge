n,m=map(int,input().split())
h=[*map(int,input().split())]
roots=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    roots[a-1].append(h[b-1])
    roots[b-1].append(h[a-1])
ans=0
for i in range(n):
    if not roots[i]:ans+=1
    elif h[i]>max(roots[i]):ans+=1
print(ans)