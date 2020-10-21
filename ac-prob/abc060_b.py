a,b,c=map(int,input().split())
i=1
r=set()
while True:
  buf=(a*i)%b
  if buf==c:
    print('YES')
    break
  if buf in r:
    print('NO')
    break
  else:
    r|={buf}
  i+=1