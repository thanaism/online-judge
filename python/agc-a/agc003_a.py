a = input()
n = a.count("N")
w = a.count("W")
s = a.count("S")
e = a.count("E")
flg = False
if n == 0 and s > 0:
    flg = True
if s == 0 and n > 0:
    flg = True
if e == 0 and w > 0:
    flg = True
if w == 0 and e > 0:
    flg = True
print("YNeos"[flg::2])
