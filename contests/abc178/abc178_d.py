s=int(input())
MOD=10**9+7
fact=[0]*s
invfact=[0]*s
fact[0]=1
for i in range(1,s):
 fact[i]=fact[i-1]*i % MOD
invfact[s-1]=pow(fact[s-1],MOD-2,MOD)
for i in range(s-1,0,-1):
 invfact[i-1]=invfact[i]*i%MOD
def nCk(n, k):
 return fact[n]*invfact[k]*invfact[n-k]
ans = 0
for n in range(1,s):
 if 3*n>s:
  break
 ans+=nCk(s-2*n-1,n-1)
 ans%=MOD
print(ans)
