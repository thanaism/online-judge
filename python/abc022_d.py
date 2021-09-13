n=int(input())
f=lambda z:(z.real,z.imag)
a=sorted([complex(*map(float,input().split())) for _ in range(n)],key=f)
b=sorted([complex(*map(float,input().split())) for _ in range(n)],key=f)
ga=sum(a)/n
gb=sum(b)/n
ma=max([abs(i-ga) for i in a])
mb=max([abs(i-gb) for i in b])
print(mb/ma)