n = int(input())
csf = [[*map(int, input().split())] + [i] for i in range(n - 1)]

ans = [0] * n
for i in range(n - 1):
    c = csf[i][0]
    s = csf[i][1]
    ans[i] += s + c
    j = i + 1
    while j < n - 1:
        c, s, f, _ = csf[j]
        if ans[i] <= s:
            ans[i] = s + c
        else:
            ans[i] = ((ans[i] + f - 1) // f) * f + c
        j += 1

for t in ans:
    print(t)
