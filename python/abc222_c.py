n,m=map(int,input().split())
a=[input() for _ in range(n<<1)]
d={'GC':1,'GP':0,'CP':1,'CG':0,'PG':1,'PC':0}
l=[[0,i] for i in range(n<<1)]
for i in range(m):
	for j in range(n):
		x,y = 2*j,2*j+1
		hx,hy = a[l[x][1]][i],a[l[y][1]][i]
		if hx==hy: continue
		if d[hx+hy]==1: l[x][0] -= 1
		else: l[y][0] -= 1
	l.sort()
for _,i in l: print(i+1)