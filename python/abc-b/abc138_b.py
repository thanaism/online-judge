n, *a = map(int, open(0).read().split())
ans = 0
for i in a:
    ans += 1 / i
print(1 / ans)
