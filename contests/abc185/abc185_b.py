n,m,t=map(int,input().split())
c=0
r=n
ans='Yes'
for _ in range(m):
    a,b=map(int,input().split())
    r-=(a-c)
    if r<=0:
        ans='No'
        break
    r=min(r+(b-a),n)
    c=b
if r<=(t-b):
    ans='No'
print(ans)