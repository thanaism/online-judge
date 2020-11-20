a,b,c=map(int,input().split())
f=lambda x:x*(x+1)//2
print(f(a)*f(b)*f(c)%998244353)