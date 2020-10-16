n, m = map(int, input().split())
if n * 2 > m:
    print(int(m // 2))
else:
    print(int(n + (m - n * 2) // 4))
