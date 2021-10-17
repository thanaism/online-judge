x = input()
m = int(input())
d = max(int(c) for c in x)

def is_ok(k):
    n = 0
    for c in x:
        n = n*k + int(c)%k
    return 1 if n<=m else 0

ok = d
ng = 1<<60
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    if is_ok(mid):
        ok=mid
    else:
        ng=mid

if len(x)==1:
    print(1 if int(x)<=m else 0)
else:
    print(ok-d)