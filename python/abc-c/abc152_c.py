n=int(input())
p=[*map(int,input().split())]
minp=200000
ans=0
for i in p:
    minp=min(minp,i)
    if i==minp:ans+=1
print(ans)