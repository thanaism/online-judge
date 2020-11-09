a,b=map(int,input().split())
ans='No'
for c in [1,2,3]:
  if (a*b*c)&1:ans='Yes'
print(ans)