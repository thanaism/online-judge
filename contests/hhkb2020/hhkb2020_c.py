"""
n=int(input())
*p,=map(int,input().split())
s=set()
for k in p:
 s|={k}
 for i in range(200001):
  if not i in s:
   print(i)
   break
"""

n = int(input())
(*p,) = map(int, input().split())
ok = [True] * 300000
min = 0
for k in p:
    ok[k] = False
    if min == k:
        while ok[min] is False:
            min += 1
    print(min)
