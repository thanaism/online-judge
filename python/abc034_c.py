w, h = map(int, input().split())

n = w + h
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
print(fact[w + h - 2] * fact_inv[w - 1] * fact_inv[h - 1] % MOD)
