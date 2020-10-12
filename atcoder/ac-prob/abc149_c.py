x=int(input())
n=10**6
b=[1]*n
b[0]=b[1]=0
m=int(-(-(n**0.5)//1))
for i in range(2,m):
  if b[i]:
    for j in range(i*i,n,i):
      b[j]=0
print(min([i for i,v in enumerate(b) if v==1 and i>=x]))