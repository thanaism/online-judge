a, b = map(int, input().split())
ans = 0
while ans * 8 // 100 != a or ans * 10 // 100 != b:
    ans += 1
    if ans > b * 100:
        ans = -1
        break
print(ans)
