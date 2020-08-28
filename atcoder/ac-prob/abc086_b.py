ab=int(open(0).read().replace(' ',''))
i=1
flg=False
while i<317:
  if i**2 == ab:
    flg=True
  i+=1
if flg:
  print('Yes')
else:
  print('No')