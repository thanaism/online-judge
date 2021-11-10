l = [*map(int, open(0))]
k = sorted(l, key=lambda x: -x % 10)
ans = 0
for i in k[:-1]:
    ans += (i + 10 - 1) // 10 * 10
ans += k[-1]
print(ans)
