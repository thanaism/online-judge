from itertools import combinations_with_replacement, permutations

n, k = map(int, input().split())
ts = [[*map(int, input().split())] for _ in range(n)]

ans = "Nothing"
for cmb in combinations_with_replacement(range(k), n):
    for p in permutations(cmb, n):
        xor = 0
        for i in range(n):
            xor ^= ts[i][p[i]]
        if xor == 0:
            ans = "Found"

print(ans)
