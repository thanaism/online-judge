a,b=input().split()
c=[a[:i]+'9'+a[i+1:] for i in range(3)]
d=[b[:i]+('0' if i>0 else '1')+b[i+1:] for i in range(3)]
c.append(a)
d.append(b)
ans=-1<<20
for i in c:
  ans=max(ans,int(i)-int(b))
for i in d:
  ans=max(ans,int(a)-int(i))
print(ans)