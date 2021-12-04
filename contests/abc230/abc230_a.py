n = int(input())
if n >= 42:
    ans = ("000" + str(n + 1))[-3:]
else:
    ans = ("000" + str(n))[-3:]
print("AGC" + ans)
