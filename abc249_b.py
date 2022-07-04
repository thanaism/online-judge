s = input()
a = [chr(ord("a") + i) for i in range(26)]
A = [chr(ord("A") + i) for i in range(26)]

has_small = False
has_large = False
for c in s:
    if c in a:
        has_small = True
    if c in A:
        has_large = True

dup = False
n = len(s)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if s[i] == s[j]:
            dup = True

print("Yes" if has_small and has_large and not dup else "No")
