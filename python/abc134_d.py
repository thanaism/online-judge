n = int(input())
a = [0] + [*map(int, input().split())]

dp = [0] * (n + 1)
dp[n] = a[n]
for i in range(n - 1, 0, -1):
    x = 2 * i
    buf = 0
    while x <= n:
        buf += dp[x]
        x += i
    if a[i] == 0 and buf & 1 == 1:
        dp[i] = 1
    if a[i] == 1 and buf & 1 == 0:
        dp[i] = 1

print(sum(dp))
print(*[i for i in range(n + 1) if dp[i]])
