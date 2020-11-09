a,k=map(int,input().split())
if k==0:
  print(2*10**12-a)
  exit()
i=0
while a<2*10**12:
  a+=a*k+1
  i+=1
print(i)

