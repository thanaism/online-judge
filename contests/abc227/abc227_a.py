n, k, a = map(int, input().split())
while k - 1:
    k -= 1
    if a == n:
        a = 1
    else:
        a += 1
print(a)
