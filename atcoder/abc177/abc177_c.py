n,*a=map(int,open(0).read().split())
c=10**9+7
sum=0
for i in range(n):
  a[i]%=c
for i in range(n-1):
  for j in range(i+1,n):
    sum+=(a[i]*a[j])%c
    sum%=c
print(sum)