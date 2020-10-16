n,k=map(int,input().split())
if n%k > k-n%k:
 print(k-n%k)
else:
 print(n%k)