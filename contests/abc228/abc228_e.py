n, k, m = map(int, input().split())
MOD = 998244353

ans = pow(m, pow(k, n, MOD - 1), MOD)
if m % MOD == 0:
    ans = 0

print(ans)
