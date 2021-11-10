a, b = map(int, input().split())
c, d = map(int, input().split())
if d != 1:
    print(0)
    exit()
elif c in [3, 5, 7, 10, 12]:
    if c == 3:
        k = 28
    else:
        k = 30
else:
    k = 31
if b == k:
    print(1)
else:
    print(0)
