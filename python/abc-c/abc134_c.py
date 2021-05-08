n,*a=map(int,open(0))
b=sorted([(v,i) for i,v in enumerate(a)])
for i in range(n):
    if i==b[-1][1]:
        print(b[-2][0])
    else:
        print(b[-1][0])
