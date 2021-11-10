n = int(input())
x, y = [], []
for _ in range(n):
    ix, iy = map(int, input().split())
    x.append(ix)
    y.append(iy)
flg = False
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if dx == 0:
                if x[i] == x[j] == x[k]:
                    flg = True
            elif dy == 0:
                if y[i] == y[j] == y[k]:
                    flg = True
            elif dx * y[k] == dy * x[k] + dx * y[i] - dy * x[i]:
                flg = True
print("Yes" if flg else "No")
