n = int(input())
s, t = [], []
for _ in range(n):
    i, j = input().split()
    s.append(i)
    t.append(j)

for i in range(n):
    cnt_s = cnt_t = 0
    for j in range(n):
        if j != i and (s[i] == s[j] or s[i] == t[j]):
            cnt_s += 1
        if j != i and (t[i] == t[j] or t[i] == s[j]):
            cnt_t += 1
    if cnt_s > 0 and cnt_t > 0:
        print("No")
        exit()
print("Yes")
