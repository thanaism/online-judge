n, k, s = map(int, input().split())

l = [1 if s == 10 ** 9 else s + 1] * n

for i in range(k):
    l[i] = s

print(*l)
