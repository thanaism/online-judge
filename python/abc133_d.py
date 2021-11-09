n = int(input())
a = [*map(int, input().split())]

l = [0] * n
l[0] = sum([-j if i & 1 else j for i, j in enumerate(a)])
for i in range(n - 1):
    l[i + 1] = 2 * a[i] - l[i]

print(*l)
