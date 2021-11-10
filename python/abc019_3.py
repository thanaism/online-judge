n = int(input())
a = [*map(int, input().split())]

for k in range(60, -1, -1):
    for i in range(n):
        d = 1 << k
        if a[i] % d == 0:
            a[i] //= d

print(len(set(a)))
