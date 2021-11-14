from collections import Counter

n = int(input())
a = [*map(int, input().split())]
q = int(input())

ca = Counter(a)
ans = sum(a)

for _ in range(q):
    b, c = map(int, input().split())
    ans -= ca[b] * b
    ans += ca[b] * c
    print(ans)
    ca[c] += ca[b]
    ca[b] = 0
