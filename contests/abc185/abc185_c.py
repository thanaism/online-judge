l=int(input())
# from itertools import combinations
# ans=combinations(range(l-1),11)
# ans=len(list(ans))
# ans=len(ans)
f=1
for i in range(l-1,l-12,-1):
    f*=i
g=1
for i in range(1,12):
    g*=i
ans=f//g
print(ans)
