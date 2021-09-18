x=input()
n=int(input())
l=[list(input()) for _ in range(n)]
d={}
r={}
for i in range(26):
	d[x[i]]=chr(ord('a')+i)
	r[chr(ord('a')+i)]=x[i]
for s in l:
	for i in range(len(s)):
		s[i]=d[s[i]]
l.sort()
for s in l:
	for i in range(len(s)):
		s[i]=r[s[i]]
for s in l:
	print(''.join(s))
