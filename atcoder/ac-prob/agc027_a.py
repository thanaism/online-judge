n, x = map(int, input().split())
a = sorted([*map(int, input().split())])
if sum(a)<x:
    print(n-1)
else:
    i = 0
    count = 0
    while i < n:
        x -= a[i]
        if x >= 0:
            count += 1
            i += 1
        else:
            break
    print(count)