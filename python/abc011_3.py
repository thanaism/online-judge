n=int(input())
l=[int(input()) for _ in range(3)]
l=set(l)
cnt=0
ans='YES'
if n in l: ans='NO'
while n>0:
	x=n-3
	while x in l or x<0:
		x+=1
	if x>n:
		ans='NO';break
	n=x;cnt+=1
	if cnt>100:
		ans='NO';break
print(ans)
		