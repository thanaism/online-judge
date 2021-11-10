n = int(input())
ans = 0
for i in range(1, n + 1):
    if ~i & 1:
        continue
    div = 0
    for j in range(1, i + 1):
        if j * j > i:
            break
        if i % j == 0:
            if i == j:
                div += 1
            else:
                div += 2
    if div == 8:
        ans += 1
print(ans)
