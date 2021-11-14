n = int(input())
a = []
DIG = 10 ** 9
for _ in range(n):
    i = 0
    s = input().split(".")
    i += int(s[0]) * DIG
    if len(s) > 1:
        i += int((s[1] + "0" * 9)[:9])
    a.append(i)

ds = {}
for i in range(n):
    two = five = 0
    x = a[i]
    while x % 2 == 0 and two < 18:
        x //= 2
        two += 1
    x = a[i]
    while x % 5 == 0 and five < 18:
        x //= 5
        five += 1
    if (two, five) not in ds:
        ds[(two, five)] = 0
    ds[(two, five)] += 1

ans = 0
for k1, v1 in ds.items():
    for k2, v2 in ds.items():
        if k1[0] + k2[0] < 18 or k1[1] + k2[1] < 18:
            continue
        if k1 == k2:
            ans += v1 * (v1 - 1)
        else:
            ans += v1 * v2

print(ans // 2)
