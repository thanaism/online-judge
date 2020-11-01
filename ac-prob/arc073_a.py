n,t=map(int,input().split())
ti=list(map(int,input().split()))
total=t
for i in reversed(range(n-1)):
  total+=t if t<ti[i+1]-ti[i] else ti[i+1]-ti[i]
print(total)