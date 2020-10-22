fib=[]
fib.append(1)
fib.append(2)
i=2
res=2
while True:
  fib.append(fib[i-1]+fib[i-2])
  if fib[i]>4000000:break
  if fib[i]%2==0:
    res+=fib[i]
  i+=1
print(res)