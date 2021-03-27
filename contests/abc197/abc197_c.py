n=int(input())
a=[*map(int,input().split())]
x=1<<31
for i in range(1<<n):
    p=q=0
    l=[0]*n
    for j in range(n):
        if i>>j&1:p=j
        l[p]|=a[j]
    for k in l:q^=k
    x=min(x,q)
print(x)
