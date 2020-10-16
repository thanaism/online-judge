import sys
sys.setrecursionlimit(10**9)
n=int(input())
memo=[-1]*(n+1)
def f(x):
 if memo[x]>0:
  return memo[x]
 if any([x==1,x==6,x==9]):
  return 1
 if x>9:
  memo[x]=min(f(x-1),f(x-6),f(x-9))+1
  return memo[x]
 elif x>6:
  memo[x]=min(f(x-1),f(x-6))+1
  return memo[x]
 else:
  memo[x]=f(x-1)+1
  return memo[x]
print(f(n))