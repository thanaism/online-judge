_,s=open(0)
res=0
for i in range(len(s)):
    count=0
    t=set()
    for l in s[:i]:
      t|={l}
    for l in t:
        if l in s[i:]:
          count+=1
    res=max(res,count)
print(res)