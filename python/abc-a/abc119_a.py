s = input()
y, m, d = s.split("/")
if int(y) < 2019:
    ans = "Heisei"
elif int(m) < 5:
    ans = "Heisei"
else:
    ans = "TBD"
print(ans)
