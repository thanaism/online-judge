n=int(input())
_t=_x=_y=0
can_exist=True
for _ in range(n):
  t,x,y=map(int,input().split())
  t,_t=t-_t,t
  x,_x=x-_x,x
  y,_y=y-_y,y
  if t<abs(x)+abs(y):
    can_exist=False
    break
  if (t-(abs(x)+abs(y)))%2==1:
    can_exist=False
    break
print('Yes' if can_exist else 'No')