s=input()
i=len(s)-1
while i>1:
  if i%2==1:
    i-=1
    continue
  if s[0:i//2]==s[i//2:i]:
    print(i)
    break
  else:
    i-=1