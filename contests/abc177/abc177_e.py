import fractions

n, *a = map(int, open(0).read().split())


def chk():
    flg = False
    flg2 = False
    ans = a[0]
    for i in range(n - 1):
        if i != 0:
            ans = fractions.gcd(ans, a[i])
        if ans != 1:
            print(ans)
            return "not coprime"
        for j in range(i + 1, n):
            if fractions.gcd(a[i], a[j]) != 1:
                flg = True
    ans = fractions.gcd(ans, a[n - 1])
    if ans != 1:
        print(ans)
        return "not coprime"
    if flg:
        return "setwise coprime"
    else:
        return "pairwise coprime"


print(chk())
