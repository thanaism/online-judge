n,k=map(int,input().split())
h=sorted([*map(int,input().split())])
print(sum(h[:max(0,n-k)]))
