"""intの各桁をリストに格納"""

"""ボツ
def to_d(x):
    digits = []
    i = 0
    buf = 0
    while True:
        buf = x % (10 ** (i + 1))
        x -= buf
        digits.append(buf // (10 ** i))
        if x == 0:
            break
        i += 1
    return digits
"""
# intならstrに変換したほうが普通に賢かった

"""
def to_d(x):
    s = str(x)
    d = []
    for i in s[::-1]:
        d += (int(i),)
    return d
"""

to_d = lambda x: [int(i) for i in str(x)[::-1]]

print(to_d(int(input())))