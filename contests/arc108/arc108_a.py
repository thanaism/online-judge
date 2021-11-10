s, p = map(int, input().split())
ans = "No"
for i in range(1, p + 1):
    if i * i > p:
        break
    if p % i == 0:
        if i + p // i == s:
            ans = "Yes"
            break
print(ans)
