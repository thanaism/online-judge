n = int(input())
s = input()

lp = [0] * n
rp = [0] * n

for i in range(n):
    if s[i] == "(":
        lp[i] = 1
    else:
        rp[i] = 1

for i in range(1, n):
    lp[i] += lp[i - 1]
    rp[i] += rp[i - 1]

left = 0
for i, j in zip(lp, rp):
    if i + left < j:
        left -= i + left - j
    right = i + left - j

print("(" * left + s + ")" * right)
