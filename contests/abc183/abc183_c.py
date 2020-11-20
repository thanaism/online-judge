n,k=map(int,input().split())
t=[[*map(int,input().split())] for _ in range(n)]
from itertools import permutations
ans=0
for p in permutations(range(n),n):
  if p[0]!=0:continue
  cost=0
  for i in range(1,n):
    cost+=t[p[i-1]][p[i]]
  cost+=t[p[-1]][0]
  if cost==k:ans+=1
print(ans)