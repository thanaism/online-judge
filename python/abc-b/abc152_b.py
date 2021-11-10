a, b = input().split()
c = a * int(b)
d = b * int(a)
print([c, d][c > d])
