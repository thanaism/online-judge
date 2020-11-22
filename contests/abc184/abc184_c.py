r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
d1=r1-c1
d2=r2-c2
s1=r1+c1
s2=r2+c2
dx=r2-r1
dy=c2-c1
sx=r1+r2
sy=c1+c2
if dx==dy==0:
    ans=0
elif s1==s2:
    ans=1
elif d1==d2:
    ans=1
elif abs(dx)+abs(dy)<=3:
    ans=1
elif s1&1==s2&1:
    ans=2
elif abs(dx)+abs(dy)<=6:
    ans=2
elif abs(d1-d2)<=3:
    ans=2
elif abs(s1-s2)<=3:
    ans=2
else:
    ans=3
print(ans)

