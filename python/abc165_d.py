a, b, n = map(int, input().split())

calc = lambda x: (a * x) // b - a * (x // b)
print(calc(min(n, b - 1)))
