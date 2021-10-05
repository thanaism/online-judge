from collections import defaultdict
n=int(input())
d=defaultdict(int)
for _ in range(n):
	a,b = map(int,input().split())
	d[a] += 1
	d[a+b] -= 1
l = sorted([*d.items()])
pre_key,pre_val = l[0]
ans=[0]*(n+1)
for i in range(1,len(l)):
	key, val = l[i]
	ans[pre_val] += key - pre_key
	pre_val += val
	pre_key = key
print(*ans[1::])