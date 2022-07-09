n, m, x, t, d = map(int, input().split())
b = t - x * d
ans = b + min(x, m) * d
print(ans)
