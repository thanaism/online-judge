from fractions import Fraction

n = int(input())
l = []
for _ in range(n):
    x, y = map(int, input().split())
    l.append((x, y))

frac = set()
x_zero = 0
y_zero = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dx = l[j][0] - l[i][0]
        dy = l[j][1] - l[i][1]
        if dy == 0:
            y_zero = 1
        elif dx == 0:
            x_zero = 1
        else:
            frac.add(Fraction(dx, dy))

print((x_zero + y_zero + len(frac)) * 2)
