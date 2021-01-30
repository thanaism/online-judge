n,s,d=map(int,input().split())
f=False
for _ in range(n):
    x,y=map(int,input().split())
    if x<s and y>d:
        f=True
if f:
    print('Yes')
else:
    print('No')