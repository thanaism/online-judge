COMP=600851475143
res=0
for i in range(2,COMP+1):
  if i*i>COMP:
    break
  is_prime=True
  for j in range(2,i+1):
    if j*j>i:break
    if i%j==0:
      is_prime=False
      break
  if is_prime and COMP%i==0:
    res=max(res,i)
print(res)