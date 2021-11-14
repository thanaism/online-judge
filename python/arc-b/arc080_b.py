h, w = map(int, input().split())
n = int(input())
a = [*map(int, input().split())]

i = row = col = 0
ans = [[0] * w for _ in range(h)]

for _ in range(h * w):
    if a[i] == 0:
        i += 1
    ans[row][col] = i + 1
    a[i] -= 1
    if (col == w - 1) and (row & 1 == 0):
        row += 1
    elif (col == 0) and (row & 1 == 1):
        row += 1
    elif row & 1 == 0:
        col += 1
    else:
        col -= 1

for i in ans:
    print(*i)
