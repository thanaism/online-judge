n=int(input())
a=[*map(int,input().split())]
m=[0]*200
for i in a:
    m[i%200]+=1
ans=0
for i in m:
    if i>0:ans+=i*(i-1)//2
print(ans)