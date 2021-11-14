n, m, k = map(int, input().split())
a = [*map(int, input().split())]
a = [i - 1 for i in a]
l = [[] for _ in range(n)]
for i in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    l[x].append((y, i))
    l[y].append((x, i))

c = [0] * (n - 1)


def dfs(f, t, p):
    if f == t:
        return 1
    for v, i in l[f]:
        if v == p:
            continue
        if dfs(v, t, f):
            c[i] += 1
            return 1
    return 0


for i in range(1, m):
    dfs(a[i - 1], a[i], -1)

s = sum(c)
if (s + k) & 1 or s + k < 0:
    print(0)
    exit()

MOD = 998244353
dp = [0] * 100001
dp[0] = 1
for i in range(n - 1):
    for j in range(100000, c[i] - 1, -1):
        dp[j] += dp[j - c[i]]
        dp[j] %= MOD
        dp[j - c[i]] %= MOD

print(dp[(s + k) >> 1])
