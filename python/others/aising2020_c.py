n = int(input())
l = 1
while l ** 2 < n:
    l += 1
ans = [0] * (n + 1)
for x in range(1, l + 1):
    for y in range(1, l + 1):
        for z in range(1, l + 1):
            k = x * (x + y) + y * (y + z) + z * (z + x)
            if k <= n:
                ans[k] += 1
for i in range(1, n + 1):
    print(ans[i])
