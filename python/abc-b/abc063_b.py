s = input()
ans = "yes"
for i in s:
    if s.count(i) != 1:
        ans = "no"
print(ans)
