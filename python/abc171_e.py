n = int(input())
a = [*map(int, input().split())]

xor = 0
for i in a:
    xor ^= i

print(*map(lambda x: x ^ xor, a))
