m=int(input())
s=[]
for _ in range(m):
    s.append(tuple(map(int,input().split())))
n=int(input())
p=set()
for _ in range(n):
    p|={tuple(map(int,input().split()))}

for i in p:
    a,b=i
    x,y=s[0]
    f=True
    for j in s:
        c,d=j
        c-=x
        d-=y
        if not (a+c,b+d) in p:
            f=False
            break
    if f:
        print(a-x,b-y)
        break