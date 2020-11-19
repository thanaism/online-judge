_,s=open(0)
ans=cnt=0
for i in s:
    cnt+=(1 if i=='I' else -1)
    ans=max(ans,cnt)
print(ans)