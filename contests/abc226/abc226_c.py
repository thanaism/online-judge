n = int(input())
tech = [0] * n
need = [set() for _ in range(n)]
have = set()
for i in range(n):
    t, k, *a = map(int, input().split())
    tech[i] = t
    for j in a:
        need[i].add(j - 1)

q = [n - 1]
ans = tech[n - 1]

while q:
    new_q = []
    for i in q:
        for j in need[i] - have:
            ans += tech[j]
            have.add(j)
            new_q.append(j)
    q = new_q

print(ans)
