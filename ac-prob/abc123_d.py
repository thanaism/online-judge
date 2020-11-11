x,y,z,k=map(int,input().split())
a=sorted([*map(int,input().split())],reverse=True)
b=sorted([*map(int,input().split())],reverse=True)
c=sorted([*map(int,input().split())],reverse=True)
ab=[]
for i in a:
  for j in b:
    ab.append(i+j)
ab.sort(reverse=True)
abc=[]
for i in ab[:k]:
  for j in c:
    abc.append(i+j)
abc.sort(reverse=True)
for i in abc[:k]:
  print(i)
