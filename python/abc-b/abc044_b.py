w = input()
ans = "Yes"
for s in list(map(chr, range(97, 123))):
    if w.count(s) % 2 != 0:
        ans = "No"
print(ans)
