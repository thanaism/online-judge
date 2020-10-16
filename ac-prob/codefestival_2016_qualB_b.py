n,a,b=map(int,input().split())
s=str(input())
o=0
e=0
for i in range(n):
  if s[i]=='a':
    if o<a+b:
      o+=1
      print('Yes')
    else:
      print('No')
  elif s[i]=='b':
    if o<a+b and e<b:
      o+=1
      e+=1
      print('Yes')
    else:
      print('No')
  else:
    print('No')
