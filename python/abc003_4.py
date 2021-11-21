r, c = map(int, input().split())
x, y = map(int, input().split())
d, l = map(int, input().split())

# Factorial Inverse library
MAX_N = r * c
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


dx = r - x + 1
dy = c - y + 1
shift = dx * dy % MOD


def calc(i, j):
    n = (x - i) * (y - j)
    r = d + l
    return 0 if n < r else nCr(n, r) * nCr(r, d) % MOD


# S
cmb = calc(0, 0)
if (x * y) != (d + l):
    # (A, B), (C, D)
    cmb -= 2 * calc(1, 0)
    cmb -= 2 * calc(0, 1)
    # (A∧B), (C∧D), (B∧C, D∧A, A∧C, B∧D)
    cmb += 1 * calc(2, 0)
    cmb += 1 * calc(0, 2)
    cmb += 4 * calc(1, 1)
    # (A∧B∧C, D∧A∧B), (B∧C∧D, C∧D∧A)
    cmb -= 2 * calc(2, 1)
    cmb -= 2 * calc(1, 2)
    # (A∧B∧C∧D)
    cmb += 1 * calc(2, 2)

print(shift * cmb % MOD)
