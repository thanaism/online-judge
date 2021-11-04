from collections import Counter

n, k = map(int, input().split())
s = input()
l = sorted(s)
ans = ""
for c in s:
    s = s[1:]
    for d in l:
        cl = Counter(l)
        cd = Counter(d)
        cs = Counter(s)
        change_count = sum((cl - cd - cs).values()) - (c == d)
        if change_count < k:
            ans += d
            k -= c != d
            l.remove(d)
            break
print(ans)
