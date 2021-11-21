s = input()

ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                t = "".join(map(str, (a, b, c, d)))
                ok = True
                for i in range(10):
                    if s[i] == "o" and str(i) not in t:
                        ok = False
                    if s[i] == "x" and str(i) in t:
                        ok = False
                if ok:
                    ans += 1

print(ans)
