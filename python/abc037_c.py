n, k = map(int, input().split())
a = [*map(int, input().split())]
b = [0]

for i in a:
    b.append(b[-1] + i)

ans = 0
for i in range(n):
    if i + k > n:
        continue
    ans += b[i + k] - b[i]
print(ans)
