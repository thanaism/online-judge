n=int(input())
s=[int(l) for l in input()]
t=[int(l) for l in input()]
cnt=0
for i in range(n):
  if s[i]!=t[i]:
    j=i+1
    while j<n and s[j]==0:
      j+=1
    if j==n:
      print(-1)
      exit()
    s[j]=0
    s[i]=(0 if s[i] else 1)
    cnt+=j-i
print(cnt)
