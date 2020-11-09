n=int(input())
a=[*map(int,input().split())]
total=sum(a)
b=[total]
for i,v in enumerate(a):
  b.append(b[i]-v)
ans=0
for i in range(len(a)):
  ans+=(a[i]*b[i+1])%1000000007
print(ans%1000000007)