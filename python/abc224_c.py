n = int(input())
x = []
y = []
for _ in range(n):
    i,j = map(int,input().split())
    x.append(i)
    y.append(j)

from itertools import combinations
ans = 0
for i,j,k in combinations(range(n),3):
    if x[i]==x[j]==x[k]: continue
    if y[i]==y[j]==y[k]: continue
    dx1 = x[i]-x[j]
    dx2 = x[k]-x[j]
    dy1 = y[i]-y[j]
    dy2 = y[k]-y[j]
    if dx2*dy1 == dx1*dy2: continue
    ans += 1

print(ans)