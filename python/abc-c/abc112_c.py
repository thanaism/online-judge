n = int(input())
l = []
for _ in range(n):
    l.append([*map(int, input().split())])

for x in range(101):
    for y in range(101):
        for i in range(n):
            if l[i][2] > 0:
                h = l[i][2] + abs(l[i][0] - x) + abs(l[i][1] - y)
        ok = True
        for i in range(n):
            if max(h - abs(l[i][0] - x) - abs(l[i][1] - y), 0) != l[i][2]:
                ok = False
        if ok:
            print(x, y, h)
            exit()
