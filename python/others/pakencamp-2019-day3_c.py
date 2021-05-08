n,m=map(int,input().split())
from itertools import combinations
ans=[]
for _ in range(n):
    a=[*map(int,input().split())]
    p=[]
    for c in combinations(range(m),2):
        i,j=c
        p.append(max(a[i],a[j]))
    ans.append(p[:])
res=0
for i in range(len(ans[0])):
    cnt=0
    for j in ans:
        cnt+=j[i]        
    res=max(res,cnt)
print(res)