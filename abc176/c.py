n=int(input())
a=list(map(int,input().split()))
top=0
sum=0
for i in range(n):
  if top < a[i]:
    top=a[i]
  sum+=top-a[i]
print(sum)
  