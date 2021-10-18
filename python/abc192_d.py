x = input()
m = int(input())
d = max(int(c) for c in x)

def is_ok(k):
    n = 0
    for c in x: n = n*k + int(c)
    return 1 if n<=m else 0

ok = d
ng = INF = 1<<60
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    if is_ok(mid):
        ok=mid
    else:
        ng=mid

print(ok-d if ok!=INF-1  else 1)