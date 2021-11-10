n = int(input())
town = []
for _ in range(n):
    town.append([*map(int, input().split())])
town.sort(key=lambda x: 2 * x[0] + x[1])
T = 0
A = sum([i[0] for i in town])
ans = 0
while True:
    ans += 1
    a, t = town.pop()
    T += a + t
    A -= a
    if T > A:
        break
print(ans)
