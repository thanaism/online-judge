a, b, k = map(int, input().split())
for i in range(k):
    if i & 1 == 0:
        a //= 2
        b += a
    else:
        b //= 2
        a += b
print(a, b)
