s = input()
ans = "None"
for i in range(97, 123):
    a = chr(i)
    if a not in s:
        ans = a
        break
print(ans)
