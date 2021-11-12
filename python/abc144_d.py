from math import degrees, atan2

a, b, x = map(int, input().split())
if 2 * x >= a * a * b:
    ans = degrees(atan2(2 * (a * a * b - x), a * a * a))
else:
    ans = degrees(atan2(a * b * b, 2 * x))

print(ans)
