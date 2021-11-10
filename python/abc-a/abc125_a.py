a, b, t = map(int, input().split())
x = ans = 0
while x + a <= t:
    x += a
    ans += b
print(ans)
