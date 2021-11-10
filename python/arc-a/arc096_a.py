a, b, c, x, y = map(int, input().split())
if y > x:
    x, y = y, x
    a, b = b, a
ans = 1 << 30
for i in range(x + 1):
    now = i * a + (x - i) * 2 * c + max(0, y - (x - i)) * b
    ans = min(ans, now)
print(ans)
