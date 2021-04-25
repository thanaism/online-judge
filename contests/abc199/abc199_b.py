n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
l=0
u=1001
for i,j in zip(a,b):
    l=max(i,l)
    u=min(j,u)
print(max(0,u-l+1))