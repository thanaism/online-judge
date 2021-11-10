import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split())
if max(n, m) - min(n, m) > 1:
    print(0)
    exit()

MOD = 10 ** 9 + 7


def frac(x):
    if x == 1:
        return 1
    return x * frac(x - 1) % MOD


if n == m:
    ans = frac(n) % MOD
    ans *= 2 * ans
    ans %= MOD
    print(ans)
else:
    print(frac(n) * frac(m) % MOD)
