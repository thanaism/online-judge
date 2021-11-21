n, k = map(int, input().split())

# Factorial Inverse library
MAX_N = n
MOD = 10 ** 9 + 7
fact = [1] * (MAX_N + 1)
inv = fact.copy()
fact_inv = fact.copy()

for i in range(2, MAX_N + 1):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    fact_inv[i] = fact_inv[i - 1] * inv[i] % MOD


def nCr(n, r):
    return fact[n] * fact_inv[n - r] * fact_inv[r] % MOD


ans = 0
for i in range(n):
    if n - i < 1 or i > k:
        break
    buf = nCr(n, i)
    buf *= nCr(n - 1, n - i - 1)
    buf %= MOD
    ans += buf
    ans %= MOD


print(ans)
