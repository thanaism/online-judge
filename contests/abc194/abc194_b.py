n=int(input())
a,b=[],[]
for i in range(n):
    ia,ib=map(int,input().split())
    a.append([ia,i])
    b.append([ib,i])
a.sort(key=lambda x:x[0])
b.sort(key=lambda x:x[0])
if a[0][1]==b[0][1]:
    c=max(a[1][0],b[0][0])
    d=max(a[0][0],b[1][0])
    print(min(a[0][0]+b[0][0],c,d))
else:
    print(max(a[0][0],b[0][0]))
        