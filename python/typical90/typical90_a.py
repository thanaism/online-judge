n,l=map(int,input().split())
k=int(input())
a=[*map(int,input().split())]
def is_ok(x,k):
    b=0
    m=0
    for i in a:
        if i-b>=x and l-i>=x:
            b=i
            m+=1
    return m>=k
ok=0
ng=l+1
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    if is_ok(mid,k):
        ok=mid
    else:
        ng=mid
print(ok)

