n, m = map(int, input().split())
imos = [0] * 110000
total = 0
for _ in range(n):
    l, r, s = map(int, input().split())
    l -= 1
    imos[l] += s
    imos[r] -= s
    total += s

for i in range(1, 100001):
    imos[i] += imos[i - 1]

ans = total - min(imos[:m])
print(ans)
