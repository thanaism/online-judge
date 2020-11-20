a,b,h,m=map(int,input().split())
import math
d=abs((h+(m/60))*30-m*6)
rad=min(d,360-d)*math.pi/180
c=a*a+b*b-2*a*b*math.cos(rad)
print(math.sqrt(c))