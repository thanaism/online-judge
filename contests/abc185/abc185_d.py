n,m=map(int,input().split())
a=sorted([*map(int,input().split())])
a.append(n+1)
b=0
d=[]
s=n
for i in a:
    l=i-b-1
    if l>0:
        d.append(l)
        s=min(s,l)
    b=i
ans=0
for i in d:
    ans+=(i+s-1)//s
# print(s,d)
print(ans)