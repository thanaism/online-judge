n,x=map(int,input().split())
s=input()
for i in s:
    if i=='o':
        x+=1
    elif i=='x':
        x=max(x-1,0)
print(x)