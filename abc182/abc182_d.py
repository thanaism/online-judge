n=int(input())
a=list(map(int,input().split()))
x=0
b=[]
y=0
c=[]
for i in a:
  x+=i
  b.append(x)
  y=max(y,x)
  c.append(y)
ans=x=0
for i,v in enumerate(b):
  ans=max(ans,x+c[i])
  x+=v
print(ans)