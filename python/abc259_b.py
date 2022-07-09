import math, cmath

a, b, d = map(int, input().split())
c = complex(a, b)
rad = cmath.phase(c)
new_rad = math.radians(math.degrees(rad) + d)
new_c = cmath.rect(abs(c), new_rad)
print(new_c.real, new_c.imag)
