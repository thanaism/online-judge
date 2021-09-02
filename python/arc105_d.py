t=int(input())
for _ in range(t):
	n=int(input())
	a=[*map(int,input().split())]
	if n&1==1:
		print('Second')
	else:
		a.sort()
		ok=True
		for i in range(1,n,2):
			if a[i]!=a[i-1]:ok=False
		if ok:
			print('Second')
		else:
			print('First')