n=int(input())
a=[*map(int,input().split())]
q=int(input())
a.sort()
m=max(a)
for _ in range(q):
    b=int(input())
    ok=-1
    ng=m
    while abs(ok-ng)>1:
        mid=(ok+ng)//2
        if mid>=b:
            ok=mid
        else:
            ng=mid
    print(min(abs(ok-b),abs(ng-b)))