n=int(input())
a=[*map(int,input().split())]

for i in range(len(a)-1):
  j=i+1
  while a[j]<a[i]:
    a[j],a[i]=a[i],a[j]
    print(a)
    j+=1

