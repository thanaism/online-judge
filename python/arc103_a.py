n=int(input())
v=[*map(int,input().split())]

d1={}
for i in v[0::2]:
	if i in d1:
		d1[i]+=1
	else:
		d1[i]=1
d2={}
for i in v[1::2]:
	if i in d2:
		d2[i]+=1
	else:
		d2[i]=1

l1=list(d1.items())
l1.sort(key=lambda x:x[1])
l2=list(d2.items())
l2.sort(key=lambda x:x[1])

INF=1<<60
a1=l1[-1][1]
a2=l2[-1][1]
b1=l1[-2][1] if len(l1)>1 else 0
b2=l2[-2][1] if len(l2)>1 else 0

t1=l1[-1][0]
t2=l2[-1][0]

if t1!=t2:
	print(n-a1-a2)
	exit()

print(n-max(
	a1+b2,
	a2+b1
))
