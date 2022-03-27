n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def f(x, y, i):
    if abs(x[i] - x[i - 1]) > k and abs(x[i] - y[i - 1]) > k:
        x[i] = -(1 << 60)


for i in range(1, n):
    f(a, b, i)
    f(b, a, i)

print("YNeos"[a[n - 1] < 0 and b[n - 1] < 0 :: 2])
