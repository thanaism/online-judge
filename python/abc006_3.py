n, m = map(int, input().split())

if not (n * 2 <= m <= n * 4):
    print(-1, -1, -1)
    exit()

d = m - n * 2
if d <= n:
    print(a := n - d, b := d, c := 0)
    assert(m == a * 2 + b * 3 + c * 4)
else:
    print(a := 0, b := 2 * n - d, c := d - n)
    assert(m == a * 2 + b * 3 + c * 4)
