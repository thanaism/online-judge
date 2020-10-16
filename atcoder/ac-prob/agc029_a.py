s=input()
w=0
d=0
for i,v in enumerate(s):
  if v=='W':
    w+=1
    d+=i
print(d-sum(range(w)))