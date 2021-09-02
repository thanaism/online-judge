n=int(input())

def dfs(s):
	if int(s)>n:
		return 0
	m = 1 if all([s.count(c) for c in '753']) else 0
	for c in '753':
		m += dfs(s+c)
	return m

print(dfs('0'))