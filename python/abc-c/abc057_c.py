n = int(input())
ans = 1 << 60
for i in range(1, n + 1):
    if i * i > n:
        break
    if n % i == 0:
        a = str(i)
        b = str(n // i)
        ans = min(ans, max(len(a), len(b)))
print(ans)
