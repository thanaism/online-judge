n = int(input())
a = [*map(int, input().split())]

ans = -(1 << 60)
for i in range(n):
    max_aoki = -(1 << 60)
    for j in range(n):
        if i == j:
            continue
        l = min(i, j)
        r = max(i, j) + 1
        aoki = sum(a[l + 1 : r : 2])
        if max_aoki < aoki:
            max_aoki = aoki
            indices = (l, r)
    l, r = indices
    ans = max(ans, sum(a[l:r:2]))

print(ans)
