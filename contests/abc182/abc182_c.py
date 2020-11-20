n=input()
l=len(n)
from itertools import combinations
for i in range(l,0,-1):
  for j in combinations(n,i):
    if sum(map(int,j))%3==0:
      print(l-i)
      exit()
print(-1)