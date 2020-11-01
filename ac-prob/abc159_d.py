n=int(input())
a=list(map(int,input().split()))
ls=[0]*n
for i in a:
  ls[i-1]+=1
total=sum([i*(i-1)//2 for i in ls])
for i in a:
  print(total-ls[i-1]+1)