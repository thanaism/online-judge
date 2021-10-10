n,p=map(int,input().split())
a=[*map(int,input().split())]
ans=sum([1 for i in a if i<p])
print(ans)