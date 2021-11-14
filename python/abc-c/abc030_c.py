n, m = map(int, input().split())
x, y = map(int, input().split())
a = [0] + [*map(int, input().split())] + [10 ** 10]
b = [0] + [*map(int, input().split())] + [10 ** 10]

i = 1
ans = 0
while i < n + 2:
    arrival = a[i] + x
    ok = m + 1
    ng = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if b[mid] >= arrival:
            ok = mid
        else:
            ng = mid
    if ok < m + 1:
        ans += 1
    else:
        break
    arrival = b[ok] + y
    ok = n + 1
    ng = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if a[mid] >= arrival:
            ok = mid
        else:
            ng = mid
    if ok < n + 1:
        i = ok
    else:
        break
print(ans)
