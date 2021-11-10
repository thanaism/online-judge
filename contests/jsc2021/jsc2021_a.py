x, y, z = map(int, input().split())
for i in range(y * z, -1, -1):
    if i * x < z * y:
        ans = i
        break
print(ans)
