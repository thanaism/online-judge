n = int(input())
c = [int(input()) for _ in range(n)]

div = [0] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if c[i] % c[j] == 0:
            div[i] += 1

total = 0
for i in div:
    if i & 1:
        total += 1 / 2
    else:
        total += (i + 2) / (2 * i + 2)

print(total)
