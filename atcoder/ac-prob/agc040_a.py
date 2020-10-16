"""
連続を数えるときに右側の連続は配列をひっくり返して数えればよい
"""

"""
S = input()
count = 0
ge = [0]
for i, v in enumerate(S):
    if v == '<':
        count += 1
    else:
        count = 0
    ge += (count,)
count = 0
le = [0]
for i, v in enumerate(S[::-1]):
    if v == '>':
        count += 1
    else:
        count = 0
    le += (count,)
ls = []
for g, l in zip(ge, le[::-1]):
    ls += (max(g, l),)
print(sum(ls))
"""

# 工夫すれば最後のループも削れる
# a[i]とa[i+1]の間がs[i]とすれば

s = input()
a = [0] * (len(s) + 1)
for i in range(len(s)):
    if s[i] == '<':
        a[i + 1] = a[i] + 1
for i in range(len(s)):
    if s[-(i + 1)] == '>':
        a[-(i + 2)] = max(a[-(i + 1)] + 1, a[-(i + 2)])
print(sum(a))