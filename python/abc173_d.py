n = int(input())
a = sorted([*map(int, input().split())], reverse=True)
ans = a[0]
for i in range(n - 2):
    ans += a[i // 2 + 1]
print(ans)
