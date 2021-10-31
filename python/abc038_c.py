n = int(input())
a = [*map(int, input().split())]

p = 0
s = set()
for i in range(n - 1):
    if a[i] >= a[i + 1]:
        s.add((p, i))
        p = i + 1
s.add((p, n - 1))

ans = 0
for i, j in s:
    ans += j - i + 1
    ans += (j - i + 1) * (j - i) // 2
print(ans)
