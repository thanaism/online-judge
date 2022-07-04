n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

t = [sum(l) for l in ab]
b = [ab[0][1]]
for i in range(1, n):
    b.append(min(b[-1], ab[i][1]))

ans = 1 << 60
base = 0
for i in range(n):
    base += t[i]
    total = base
    d = x - i - 1
    if d < 0:
        break
    total += d * b[i]
    ans = min(ans, total)

print(ans)
