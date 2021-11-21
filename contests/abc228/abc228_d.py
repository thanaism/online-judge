n = 1 << 20
q = int(input())

a = [-1] * n
p = [0] * n
for i in range(n):
    p[i] = (i + 1) % n

for _ in range(q):
    t, x = map(int, input().split())
    if t == 2:
        ans = a[x % n]
        print(ans)
    else:
        y = x
        use = set()
        while a[x % n] != -1:
            use.add(x % n)
            x = p[x % n]
        for i in use:
            p[i] = x % n
        a[x % n] = y
