from collections import deque
a = [ [*map(int,input().split())] for _ in range(4) ]
vs = { (i,j) for i in range(4) for j in range(4) if a[i][j] }
ans = 0
for i in range(1<<16):
	ok = True
	on  = [[False]*4 for _ in range(4)]
	st_on = set()
	off = [[True]*6 for _ in range(6)]
	st_off = {(i,j) for i in range(6) for j in range(6)}
	for j in range(16):
		r = j//4
		c = j%4
		if (r,c) in vs and i>>j&1==0:
			ok = False
		if i>>j&1==1:
			on[r][c] = True
			st_on.add((r,c))
			off[r+1][c+1] = False
			st_off.remove((r+1,c+1))
	if len(st_on)==0: continue
	q = deque()
	q.append(st_on.pop())
	di = [0,1,0,-1]
	dj = [1,0,-1,0]
	while q:
		a,b = q.popleft()
		for k in range(4):
			ni = a+di[k]
			nj = b+dj[k]
			if ni<0 or ni>=4 or nj<0 or nj>=4: continue
			if not on[ni][nj] or (ni,nj) not in st_on: continue
			q.append((ni,nj))
			st_on.remove((ni,nj))
	if len(st_on): ok = False
	q = deque()
	q.append(st_off.pop())
	while q:
		a,b = q.popleft()
		for k in range(4):
			ni = a+di[k]
			nj = b+dj[k]
			if ni<0 or ni>=6 or nj<0 or nj>=6: continue
			if not off[ni][nj] or (ni,nj) not in st_off: continue
			q.append((ni,nj))
			st_off.remove((ni,nj))
	if len(st_off): ok = False
	if ok: ans+=1
print(ans)