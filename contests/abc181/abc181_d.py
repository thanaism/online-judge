s = input()
i = 0
ls = []
while True:
    i += 8
    if i >= 1000:
        break
    if "0" not in str(i):
        if len(s) == 1:
            if not len(str(i)) == 1:
                continue
        elif len(s) == 2:
            if not len(str(i)) == 2:
                continue
        elif len(s) >= 3:
            if not len(str(i)) == 3:
                continue
        ls.append(str(i))
res = False
for i in ls:
    flg = [False] * len(i)
    for j in s:
        for k, v in enumerate(i):
            if v == j and flg[k] == False:
                flg[k] = True
                break
    if all(flg):
        res = True
        break
print("Yes" if res else "No")
