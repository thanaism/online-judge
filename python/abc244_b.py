n = int(input())
t = input()
p = 0j
d = 1
for c in t:
    if c == "S":
        p += d
    if c == "R":
        d *= -1j
print(p.real, p.imag)
