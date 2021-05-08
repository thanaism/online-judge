n,d=map(int,input().split())
x=[]
for _ in range(n):
        x.append([*map(int,input().split())])
ans=0
for i in range(n):
    for j in range(i+1,n):
        dist=0
        for p,q in zip(x[i],x[j]):
            dist+=(p-q)**2
        for k in range(dist+1):
            if k*k==dist:ans+=1
print(ans)