import math
a,b=10,35

# 34Byte
lcm=lambda x,y: x*y//math.gcd(x,y)

# 41Byte
def LCM(x,y):
  return x*y//math.gcd(x,y)

print(math.gcd(a,b),lcm(a,b))