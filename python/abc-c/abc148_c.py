a, b = map(int, input().split())


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


c = gcd(a, b)
print(a // c * b // c * c)
