n,x,*l=map(int,open(0).read().split())
m=[0]
for i in l:
    k=i+m[-1]
    if k>x:break
    m.append(k)
print(len(m))
