s = input()
n = len(s)

ans = [0] * n

right_e = 0
right_o = 0
for i in range(n):
    if s[i] == "R":
        right_o += 1
        right_o, right_e = right_e, right_o
    else:
        ans[i - 1] += right_e
        ans[i] += right_o
        right_e = right_o = 0

left_e = 0
left_o = 0
for i in range(n - 1, -1, -1):
    if s[i] == "L":
        left_o += 1
        left_o, left_e = left_e, left_o
    else:
        ans[i + 1] += left_e
        ans[i] += left_o
        left_e = left_o = 0

print(*ans)
