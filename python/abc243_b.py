n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
sa = set(a)
sb = set(b)
s = sa & sb
ans = 0
for i, j in zip(a, b):
    if i == j:
        ans += 1

print(ans)
print(len(s) - ans)
