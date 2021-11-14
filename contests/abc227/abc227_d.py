n, k = map(int, input().split())
a = [*map(int, input().split())]

is_ok = lambda x: x * k <= sum([min(i, x) for i in a])

ok = 0
ng = 1 << 60
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
