a, b, w = map(int, input().split())
w *= 1000
ma = w // a
mi = (w + b - 1) // b
if mi > ma:
    print("UNSATISFIABLE")
else:
    print(mi, ma)
