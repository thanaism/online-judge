n,m,c = map(int,input().split())
b,*a = [list(map(int,input().split())) for _ in range(n+1)]
res=0
for i in range(n):
  sum=0
  for j in range(m):
    sum+=a[i][j]*b[j]
  if sum+c>0:
    res+=1
print(res)