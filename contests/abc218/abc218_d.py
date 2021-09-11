n=int(input())
st=set()
ls=[]
for _ in range(n):
	tp=tuple(map(int,input().split()))
	st.add(tp)
	ls.append(tp)

ans=0
for a in ls:
	for b in ls:
		# print(a,b)
		if a[0]==b[0] or a[1]==b[1]: continue
		xa,ya=a
		xb,yb=b
		# print(xa,xb,ya,yb)
		if xa>xb:
			xa,xb=xb,xa
			ya,yb=yb,ya
		ok=True
		if (xb,ya) not in st: ok=False
		if (xa,yb) not in st: ok=False
		if ok: ans+=1
		
print(ans//4)