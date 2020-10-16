n=int(input())
if (n+1)//1.08 != n//1.08:
  res = int((n+1.08)//1.08)
  print(res)
else:
  print(':(')