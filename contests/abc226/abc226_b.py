n = int(input())
s = set()
for _ in range(n):
    _, *j = map(int, input().split())
    s.add(tuple(j))
print(len(s))
