a, b, c, d = map(int, input().split())
while a > 0 and c > 0:
    c -= b
    a -= d
print("No" if c > 0 and a <= 0 else "Yes")
