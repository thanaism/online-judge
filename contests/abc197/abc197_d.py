from math import *

n = int(input())
x0, y0 = map(int, input().split())
x2, y2 = map(int, input().split())
xo, yo = x0 + (x2 - x0) / 2, y0 + (y2 - y0) / 2
x, y = x0 - xo, y0 - yo
t = 2 * pi / n
a = x * cos(t) - y * sin(t)
b = x * sin(t) + y * cos(t)
print(a + xo, b + yo)
