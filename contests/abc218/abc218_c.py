n = int(input())
s = [complex(i, j) for i in range(n) for j, k in enumerate(input()) if k == "#"]
t = [complex(i, j) for i in range(n) for j, k in enumerate(input()) if k == "#"]
ans = "No"
for _ in range(4):
    t = [z * 1j for z in t]
    t.sort(key=lambda z: (z.real, z.imag))
    d = s[0] - t[0]
    t = [z + d for z in t]
    if s == t:
        ans = "Yes"
print(ans)
