a,b,c=map(int,input().split())
if a==b==c and a%2==0:
  print(-1)
else:
  d=a|b|c
  print(len(bin(d&-d))-3)