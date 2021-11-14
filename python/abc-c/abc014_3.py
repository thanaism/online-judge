n = int(input())
imos = [0] * 1100000
for _ in range(n):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[b + 1] -= 1

for i in range(1, 1000001):
    imos[i] += imos[i - 1]

print(max(imos))
