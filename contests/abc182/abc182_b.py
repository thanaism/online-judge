n=int(input())
a=list(map(int,input().split()))
maximum=0
for i in range(2,1001):
  cnt=0
  for j in a:
    if j%i==0:cnt+=1
  if cnt>maximum:
    maximum=cnt
    ans=i
print(ans)