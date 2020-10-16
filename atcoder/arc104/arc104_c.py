n=int(input())
a=[None]*n
b=[None]*n
c=[None]*n
s=set(range(1,2*n+1))
for i in range(n):
 a[i],b[i]=map(int,input().split())
 if any([a[i]==-1,b[i]==-1]):
  c[i]=-1
 else:
  if a[i]>=b[i]:
   print('No')
   exit()
  c[i]=b[i]-a[i]-1
 if a[i]!=-1:
  if a[i] in s:
   s-={a[i]}
  else:
   print('No')
   exit()
 if b[i]!=-1:
  if b[i] in s:
   s-={b[i]}
  else:
   print('No')
   exit()
print(s)