from itertools import permutations

s = input()

st = set()
for p in permutations(s, len(s)):
    st.add("".join(p))

print(len(st))
