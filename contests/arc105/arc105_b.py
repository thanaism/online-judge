from math import gcd
from functools import reduce
n=int(input())
a = [*map(int,input().split())]
print(reduce(gcd,a))
# print(reduce(lambda x,y:(x*y)//gcd(x,y),a,1))