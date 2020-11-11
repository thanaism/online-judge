_,h=open(0)
*h,=map(int,h.split())
ans=0
for i in range(1,101):
  flg=False
  for j in h:
    if j>=i:
      flg=True
    elif flg:
      ans+=1
      flg=False
  if flg:ans+=1
print(ans)