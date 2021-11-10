n = int(input())
s = [input() for _ in range(n)]

leading_b = set()
trailing_a = set()

ab = 0
for i in range(n):
    if s[i][0] == "B":
        leading_b.add(i)
    if s[i][-1] == "A":
        trailing_a.add(i)
    ab += s[i].count("AB")

n_a = len(trailing_a)
n_b = len(leading_b)
d = min(n_a, n_b)
if trailing_a == leading_b:
    d -= 1
print(ab + max(0, d))
