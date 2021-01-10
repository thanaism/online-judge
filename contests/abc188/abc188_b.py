n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
ans=sum([i*j for i,j in zip(a,b)])
if ans==0:
    print('Yes')
else:
    print('No')