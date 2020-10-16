T=X=Y=0
for _ in[0]*int(input()):
 t,x,y=map(int,input().split())
 d,T,X,Y=abs(x-X)+abs(y-Y),t-T,x,y
 if T<d or(d-T)&1:print('No');exit()
 T=t
print('Yes')