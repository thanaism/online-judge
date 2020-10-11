"""
t=int(input())
for _ in range(t):
 n=int(input())
 a=[*input().split()]
 if n%2==0:
  if a.count('1')%2==0:
   print('Second')
  else:
   print('First')
 else:
  if a.count('1')%2==0:
   print('Second')
  else:
   print('First')
"""

t=int(input())
for _ in range(t):
 n=int(input())
 a=[*map(int,input().split())]
 if n%2==0:
  if sum([1 for i in a if i%2==1])%2==0:
   print('Second')
  else:
   print('First')
 else:
  if sum([1 for i in a if i%2==1])%2==0:
   print('Second')
  else:
   print('First')
