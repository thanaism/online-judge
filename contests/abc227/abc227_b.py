n = int(input())
s = [*map(int, input().split())]

st = set()
for a in range(1, 1001):
    for b in range(1, 1001):
        tmp = 4 * a * b + 3 * a + 3 * b
        st.add(tmp)

ans = 0
for i in s:
    if i not in st:
        ans += 1

print(ans)
