n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = INF = 1 << 60


def solve(t, ls):
    if len(ls) == 0:
        return INF
    return abs(sum(ls) - t) + 10 * (len(ls) - 1)


from itertools import product

for p in product(range(4), repeat=n):
    x, y, z = [], [], []
    for i in range(n):
        if p[i] == 1:
            x.append(l[i])
        if p[i] == 2:
            y.append(l[i])
        if p[i] == 3:
            z.append(l[i])
    ans = min(ans, solve(a, x) + solve(b, y) + solve(c, z))

print(ans)
