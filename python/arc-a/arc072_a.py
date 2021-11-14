n = int(input())
a = [*map(int, input().split())]

for i in range(1, n):
    a[i] += a[i - 1]

ans = 1 << 60
for flg in (True, False):
    err = 0
    buf = 0
    for i in range(n):
        v = a[i] + err
        if ((v > 0) != flg) or v == 0:
            if v == 0:
                if flg:
                    err += 1
                    buf += 1
                else:
                    err -= 1
                    buf += 1
            elif flg:
                err += -(v - 1)
                buf += -(v - 1)
            else:
                err += -(v + 1)
                buf += +(v + 1)
        flg = not flg
    ans = min(ans, buf)

print(ans)
