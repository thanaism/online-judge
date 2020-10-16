n,m,x=map(int,input().split())
a=[*map(int,input().split())]
s=sum([1 for i in a if i>x])
t=sum([1 for i in a if i<x])
print(min(t,s))