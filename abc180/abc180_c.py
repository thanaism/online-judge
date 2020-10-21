n=int(input())
i=1
l=set()
while i*i<=n:
  if n%i==0:
    l.update({i})
    l.update({n//i})
  i+=1
for d in sorted(l):
  print(d)