n = int(input())
taka, aoki = map(int, input().split())
for _ in range(n - 1):
    t, a = map(int, input().split())
    k1 = (taka + t - 1) // t
    k2 = (aoki + a - 1) // a
    k = max(k1, k2)
    taka = t * k
    aoki = a * k
print(taka + aoki)
