n=int(input())
ss=[input()[::-1] for _ in range(n)]
ss.sort(key=len)
from collections import defaultdict
d=defaultdict(lambda:[0]*26)
p=(1<<61)-1
ans=0
for s in ss:
	i=ord(s[-1])-97
	a=0
	t=[0]*26
	for c in s[:-1]:
		j=ord(c)-97
		if a in d:
			for k in range(26):
				t[k]+=d[a][k]
		ans+=t[j]
		t[j]=0
		a=(a*27+j+1)%p
	ans+=t[i]
	d[a][i]+=1
print(ans)
	
