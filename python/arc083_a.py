a,b,c,d,e,f=map(int,input().split())

ok=[[False]*(3001) for _ in range(3001)]
ok[0][0]=True
nax=0
ans1=100*a
ans2=0
for total in range(1,f+1):
	for sugar in range(1,total+1):
		water=total-sugar
		if 100*a<=total and ok[total-100*a][sugar]:
			ok[total][sugar]=True
		if 100*b<=total and ok[total-100*b][sugar]:
			ok[total][sugar]=True
		if c<=total and c<=sugar and ok[total-c][sugar-c]:
			ok[total][sugar]=True
		if d<=total and d<=sugar and ok[total-d][sugar-d]:
			ok[total][sugar]=True
        
		if sugar*100<=water*e and ok[total][sugar] and 0<sugar:
			p=100*sugar/total
			if nax<p:
				nax=p
				ans1=total
				ans2=sugar
print(ans1,ans2)
		