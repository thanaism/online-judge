n = int(input())

ans = 0
for i in range(1, n + 1):
    if i * i * i > n:
        break
    for j in range(i, n + 1):
        if i * j * j > n:
            break
        ans += n // (i * j)
        ans -= j
        ans += 1
print(ans)
