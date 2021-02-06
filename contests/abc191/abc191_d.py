# from math import sqrt
# x,y,r=map(float,input().split())
# if r==0:
#     if int(x)==x and int(y)==y:
#         print(1)
#     else:
#         print(0)
#     exit()
# max_x=int(x+r)
# min_x=int(-((x-r)//-1))
# ans=0
# if min_x>max_x:
#     if int(x)==x and int(y)==y: 
#         print(1)
#     else:
#         print(0)
#     exit()
# for i in range(min_x,max_x+1):
#     if abs(r)==abs(x-i) and int(y)==y:
#         ans+=1
#     else:
#         rt=sqrt(r*r-(x-i)*(x-i))
#         max_y=int(y+rt)
#         min_y=int(-((y-rt)//-1))
#         if max_y>=min_y:
#             ans+=int(max_y-min_y+1)
# print(ans)
# x,y,r=map(lambda x:int(float(x)*z),input().split())
from decimal import Decimal
from math import isqrt
z=10000
x,y,r=map(lambda x:int(Decimal(x)*z),input().split())
max_x=(x+r)//z
min_x=(x-r)//z
ans=0
for i in range(min_x,max_x+2):
    yy=r**2-(i*z-x)**2
    if yy<0:continue
    rt=isqrt(yy)
    max_y=(y+rt)//z
    min_y=(y-rt+z-1)//z
    ans+=max_y-min_y+1
print(ans)