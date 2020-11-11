n=int(input())
a=[*map(int,input().split())]
ans=right=SUM=XOR=0
for left in range(n):
  right=max(right,left)
  while right<n and SUM+a[right]==XOR^a[right]:
    SUM+=a[right]
    XOR^=a[right]
    right+=1
  ans+=right-left
  SUM-=a[left]
  XOR^=a[left]
print(ans)
