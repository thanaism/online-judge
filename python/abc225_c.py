n, m = map(int, input().split())
b = [[*map(int, input().split())] for _ in range(n)]

ok = True
for i in range(n):
    for j in range(m):
        if b[i][j] == 0:
            ok = False
            break
        if j + 1 < m:
            if b[i][j] + 1 != b[i][j + 1]:
                ok = False
                break
            if b[i][j] % 7 == 0 and b[i][j + 1] % 7 == 1:
                ok = False
                break
        if i + 1 < n and b[i][j] + 7 != b[i + 1][j]:
            ok = False
            break
if ok:
    print("Yes")
else:
    print("No")
