n=int(input())
if n==0:
	print(0)
	exit()
b=1
m=2
ans=''
while n!=0:
	if n%m==0:
		ans+='0'
	else:
		ans+='1'
		n-=b
	b *= -2
	m *= 2
ans=ans[::-1]
print(ans)