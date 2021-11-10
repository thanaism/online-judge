k = int(input())


def gcd(a, b, c):
    while b > 0:
        a, b = b, a % b
    while c > 0:
        a, c = c, a % c
    return a


ans = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        for k in range(1, k + 1):
            ans += gcd(i, j, k)
print(ans)
