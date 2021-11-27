a, b = input().split()

n = min(len(a), len(b))
a = a[::-1]
b = b[::-1]

ans = "Easy"
for i in range(n):
    ia = int(a[i])
    ib = int(b[i])
    if ia + ib > 9:
        ans = "Hard"

print(ans)
