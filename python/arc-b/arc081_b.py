n = int(input())
s1 = input()
s2 = input()

MOD = 10 ** 9 + 7
pre = -1
ans = 1
i = 0
while i < n:
    if s1[i] == s2[i]:
        if pre < 0:
            ans *= 3
        if pre == 0:
            ans *= 2
        if pre == 1:
            ans *= 1
        ans %= MOD
        i += 1
        pre = 0
    else:
        if pre < 0:
            ans *= 6
        if pre == 0:
            ans *= 2
        if pre == 1:
            ans *= 3
        ans %= MOD
        i += 2
        pre = 1

print(ans)
