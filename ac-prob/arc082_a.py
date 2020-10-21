n=int(input())
a=sorted(list(map(int,input().split())))
ls=[0]*110000
for i in a:
  ls[i]+=1
res=0
for i in range(1,100000):
  res=max(res,ls[i-1]+ls[i]+ls[i+1])
print(res)