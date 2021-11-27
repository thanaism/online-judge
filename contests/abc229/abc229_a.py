s1 = input()
s2 = input()

if s1.count("#") == 0 or s2.count("#") == 0:
    ans = "Yes"
else:
    ok = False
    for i in range(2):
        if s1[i] == s2[i] == "#":
            ok = True
    if ok:
        ans = "Yes"
    else:
        ans = "No"

print(ans)
