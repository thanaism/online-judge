n, x = map(int, input().split())
a = [*map(int, input().split())]

ans = 0
for i in range(1, n):
    d = a[i - 1] + a[i] - x
    if d > 0:
        if a[i] > d:
            a[i] -= d
        else:
            a[i - 1] -= d - a[i]
            a[i] = 0
        ans += d

print(ans)
