"""n=int(input())
from collections import defaultdict
shops=defaultdict(list)
sl=set()
for i in range(n):
    s,p=input().split()
    p=int(p)
    sl|={s}
    shops[s].append([p,i+1])
for i in sorted(sl):
    for j in sorted(shops[i],reverse=True):
        print(j[1])"""

print(*sorted(range(1,int(input())+1),key=lambda _:[(s,-int(p))for s,p in[input().split()]]))