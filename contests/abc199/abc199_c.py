n=int(input())
s=input()
l=[c for c in s]
q=int(input())
r=False
for _ in range(q):
    t,a,b=map(int,input().split())
    a-=1;b-=1
    if r:a,b=(a+n)%(n+n),(b+n)%(n+n)
    if t==1:
        l[a],l[b]=l[b],l[a]
    else:
        r=not r
if r:l=l[n:]+l[:n]
print(''.join(l))