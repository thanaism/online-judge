n, q = map(int, input().split())
a = [0] * n
for _ in range(q):
    l, r, t = map(int, input().split())
    for i in range(l - 1, r):
        a[i] = t
for i in a:
    print(i)
