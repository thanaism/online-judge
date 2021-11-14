n, k = map(int, input().split())

ans = 1
ans += 6 * (k - 1) * (n - k)
ans += 3 * (k - 1)
ans += 3 * (n - k)
ans /= n ** 3
print(ans)
