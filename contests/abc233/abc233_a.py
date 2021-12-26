x, y = map(int, input().split())
ans = (max(y - x, 0) + 9) // 10
print(ans)
