n=int(input())
p=[*map(int,input().split())]
q=[*map(int,input().split())]
from itertools import permutations
for i,v in enumerate(permutations(range(1,n+1))):
    if all([True if t==p[j] else False for j,t in enumerate(v)]):a=i
    if all([True if t==q[j] else False for j,t in enumerate(v)]):b=i
print(abs(a-b))