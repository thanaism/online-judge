n=int(input())
a,b=-1,-1
for i in range(1,100):
  for j in range(1,100):
    if n==3**i+5**j:
      a,b=i,j
      break
if a==-1:
  print(-1)
else:
  print(a,b)