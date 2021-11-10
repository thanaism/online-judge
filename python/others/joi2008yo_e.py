def main():
    r, c = map(int, input().split())
    l = []
    for _ in range(r):
        l.append([*map(int, input().split())])
    ans = 0
    for i in range(1 << r):
        x = 0
        for j in range(c):
            y = 0
            for k in range(r):
                if (i >> k) & 1:
                    y += (1, 0)[l[k][j]]
                else:
                    y += l[k][j]
            x += max(y, r - y)
        ans = max(ans, x)
    return ans


print(main())
