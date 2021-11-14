n = int(input())

x = n
d = {}
for i in range(2, n):
    if i * i >= n:
        break
    cnt = 0
    while x % i == 0:
        x //= i
        cnt += 1
    if cnt:
        d[i] = cnt

if x != 1:
    ans = 1
else:
    ans = 0

for key in d:
    i = 1
    # while i <= d[key]:
    #     ans += 1
    #     d[key] -= i
    #     i += 1
    while (i + 1) * i // 2 <= d[key]:
        i += 1
    ans += i - 1


print(ans)
