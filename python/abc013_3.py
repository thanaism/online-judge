n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())

if h - n * e > 0:
    print(0)
    exit()

lack = n * e - h
rich_diff = e + b
poor_diff = e + d

ans = 1 << 60
for poor_days in range(n + 1):
    remain = lack - poor_days * poor_diff
    cost = poor_days * c
    if remain >= 0:
        cost += (remain // rich_diff + 1) * a
    ans = min(ans, cost)

print(ans)
