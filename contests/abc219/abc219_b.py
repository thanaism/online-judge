l = [input() for _ in range(3)]
t = input()
ans = ""
for c in t:
    if c == "1":
        ans += l[0]
    if c == "2":
        ans += l[1]
    if c == "3":
        ans += l[2]
print(ans)
