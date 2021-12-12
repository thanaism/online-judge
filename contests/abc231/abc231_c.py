n, q = map(int, input().split())
a = sorted([*map(int, input().split())] + [0, 10 ** 10])
for _ in range(q):
    x = int(input())
    ok = n + 1
    ng = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if a[mid] >= x:
            ok = mid
        else:
            ng = mid
    print(n + 1 - ok)
