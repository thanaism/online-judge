n, a, b = map(int, input().split())
x = [*map(int, input().split())]

ans = 0
for i in range(1, n):
    cost = a * (x[i] - x[i - 1])
    if b < cost:
        ans += b
    else:
        ans += cost
print(ans)
