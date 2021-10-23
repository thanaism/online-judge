from collections import deque

def solve(n,a):
	endpoints = {} #defaultdict(list)
	indegrees = {} #defaultdict(int)
	for i in range(n):
		for j in range(n-2):
			s,t,u = i+1,a[i][j],a[i][j+1]
			x = (s,t) if s<t else (t,s)
			y = (s,u) if s<u else (u,s)
			if x in endpoints:
				endpoints[x].append(y)
			else:
				endpoints[x] = [y]
			if y in indegrees:
				indegrees[y] += 1
			else:
				indegrees[y] = 1

	q = deque()
	for i in range(n):
		for j in range(i+1,n):
			k = (i+1,j+1)
			if k not in indegrees or indegrees[k]==0:
				q.append(k)
	s = set()
	cnt = 0
	ans = 1
	while q:
		i = q.popleft()
		x,y = i
		if x in s or y in s:
			s = set()
			ans += 1
		s.add(x); s.add(y)
		cnt += 1
		if i not in endpoints: continue
		for j in endpoints[i]:
			indegrees[j] -= 1
			if indegrees[j]==0:
				q.append(j)
				
	if n*(n-1)//2>cnt: ans = -1
	print(ans)

def main():
	n = int(input())
	a = [[*map(int,input().split())] for _ in range(n)]
	solve(n,a)

if __name__ == '__main__':
	main()