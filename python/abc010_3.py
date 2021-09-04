sx,sy,gx,gy,t,v=map(int,input().split())
n=int(input())
ans='NO'
for i in range(n):
	x,y=map(int,input().split())
	a=abs(sx-x)**2+abs(sy-y)**2
	b=abs(gx-x)**2+abs(gy-y)**2
	if a**0.5+b**0.5<=t*v: ans='YES'

print(ans)
	
