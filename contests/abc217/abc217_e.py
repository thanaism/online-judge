from heapq import *
from collections import deque
h=[]
d=deque()
q=int(input())
for _ in range(q):
	a=[*map(int,input().split())]
	if a[0]==1:
		x=a[1]
		d.append(x)
	elif a[0]==2:
		if h:
			print(heappop(h))
		else:
			print(d.popleft())
	elif a[0]==3:
		while d:
			heappush(h,d.pop())