n=int(input())
a=[0]*46
a[0]=1
a[1]=1
if n>1:
    for i in range(2,n+1):
        a[i]=a[i-2]+a[i-1]
print(a[n])