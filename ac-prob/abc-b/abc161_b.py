n,m=map(int,input().split())
a=[*map(int,input().split())]
total=sum(a)
limit=total/4/m
ok=0
ans='No'
for i in a:
    if i<limit:continue
    ok+=1
    if ok>=m:
        ans='Yes'
        break
print(ans)