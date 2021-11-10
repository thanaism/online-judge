n = int(input())
ans = n
for i in range(1, n + 1):
    if i * i > n:
        break
    if n % i == 0:
        ans = min(n // i, ans)
print(ans + n // ans - 2)
