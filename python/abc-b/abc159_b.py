s = input()
n = len(s)
ans = "Yes"
for i, j in zip(s, s[::-1]):
    if i != j:
        ans = "No"
for i, j in zip(s[: (n - 1) // 2], s[(n - 1) // 2 - 1 : -1 : -1]):
    if i != j:
        ans = "No"
for i, j in zip(s[(n + 3) // 2 - 1 :], s[-1 : (n + 3) // 2 - 2 : -1]):
    if i != j:
        ans = "No"
print(ans)
