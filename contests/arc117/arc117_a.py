a, b = map(int, input().split())
c = list(range(-a, 0))
d = list(range(1, b + 1))
d[-1] -= sum(c) + sum(d)
assert sum(c + d) == 0
assert sum([1 for i in c if i < 0]) == b
assert sum([1 for i in d if i > 0]) == a
print(*(c + d))
