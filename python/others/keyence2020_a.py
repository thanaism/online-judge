h, w, n = map(int, open(0))
x = max(h, w)
print((n + x - 1) // x)
