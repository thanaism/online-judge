x, y, a, b = map(int, input().split())
ex = 0
while x * a < y and x * a < x + b:
    ex += 1
    x *= a
ex += (y - 1 - x) // b
print(ex)
