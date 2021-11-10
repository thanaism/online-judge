n = int(input())
a = [*map(int, input().split())]
b = [a[0]]
c = [a[0] ** 2]
for i in range(1, n):
    b.append(b[-1] + a[i])
    c.append(c[-1] + a[i] ** 2)
ans = 0
for i in range(1, n):
    x = i * (a[i] ** 2)
    y = -2 * a[i] * b[i - 1]
    z = c[i - 1]
    ans += x + y + z
print(ans)
