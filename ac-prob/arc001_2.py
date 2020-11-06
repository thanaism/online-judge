a,b=map(int,input().split())
c=0
l=(10,-10,5,-5,1,-1)
while a!=b:
  t=a
  for i in l:
    d=abs(a+i-b)
    if d<abs(b-t):t=a+i
  a=t
  c+=1
print(c)
