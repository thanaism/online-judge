# from math import *
# r,x,y=map(int,input().split())
# d=sqrt(x*x+y*y)
# if d<r:
#     print(2)
# else:
#     print(ceil(d/r))
r, x, y = map(int, input().split())
dd, rr = x * x + y * y, r * r
if dd < rr:
    print(2)
else:
    ok = 200000
    ng = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if mid ** 2 >= dd / rr:
            ok = mid
        else:
            ng = mid
    print(ok)
