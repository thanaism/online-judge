h, w, n, m = map(int, input().split())

grid = [["."] * w for _ in range(h)]
u = [[0] * w for _ in range(h)]
d = [[0] * w for _ in range(h)]
r = [[0] * w for _ in range(h)]
l = [[0] * w for _ in range(h)]

for _ in range(n):
    ia, ib = map(int, input().split())
    grid[ia - 1][ib - 1] = "*"

for _ in range(m):
    ic, id = map(int, input().split())
    grid[ic - 1][id - 1] = "#"

for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            continue
        if grid[i][j] == "*" or d[i][j] == 1:
            d[i][j] = 1
            if i + 1 < h and grid[i + 1][j] != "#":
                d[i + 1][j] = 1
        if grid[i][j] == "*" or l[i][j] == 1:
            l[i][j] = 1
            if j + 1 < w and grid[i][j + 1] != "#":
                l[i][j + 1] = 1

for i in range(h - 1, -1, -1):
    for j in range(w - 1, -1, -1):
        if grid[i][j] == "#":
            continue
        if grid[i][j] == "*" or u[i][j] == 1:
            u[i][j] = 1
            if i - 1 >= 0 and grid[i - 1][j] != "#":
                u[i - 1][j] = 1
        if grid[i][j] == "*" or r[i][j] == 1:
            r[i][j] = 1
            if j - 1 >= 0 and grid[i][j - 1] != "#":
                r[i][j - 1] = 1

light = [[0] * w for _ in range(h)]
total = 0
for i in range(h):
    for j in range(w):
        if u[i][j] > 0 or d[i][j] > 0 or r[i][j] > 0 or l[i][j] > 0:
            total += 1
            light[i][j] = 1

print(total)

# for i in range(h):
#   for j in range(w):
#     print(grid[i][j],end='')
#   print()

# print()
# for i in range(h):
#   for j in range(w):
#     print(light[i][j],end='')
#   print()
# print()
# for i in range(h):
#   for j in range(w):
#     print(u[i][j],end='')
#   print()
# print()
# for i in range(h):
#   for j in range(w):
#     print(d[i][j],end='')
#   print()
# print()
# for i in range(h):
#   for j in range(w):
#     print(l[i][j],end='')
#   print()
# print()
# for i in range(h):
#   for j in range(w):
#     print(r[i][j],end='')
#   print()
