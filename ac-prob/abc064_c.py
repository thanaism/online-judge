n=int(input())
a=[*map(int,input().split())]
c=[(i if i<3200 else 3200)//400 for i in a]
free=sum([1 for i in c if i==8])
s=set(c)
if free>0:
  MIN=1 if len(s)==1 else len(s)-1
  MAX=len(s)+free-1
else:
  MIN=len(s)
  MAX=len(s)
print(MIN,MAX)