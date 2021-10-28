from itertools import groupby

n = int(input())
a = [*map(int, input().split())]

b = []
for i in range(n):
    left = i
    right = n - i - 1
    b.append(abs(left - right))

a.sort()
b.sort()
if a != b:
    print(0)
else:
    ans = 1
    MOD = 10 ** 9 + 7
    for _, g in groupby(b):
        ans *= len(list(g))
        ans %= MOD
    print(ans)
