k = int(input())
if k & 1:
    print(k // 2 * (k // 2 + 1))
else:
    print((k // 2) ** 2)
