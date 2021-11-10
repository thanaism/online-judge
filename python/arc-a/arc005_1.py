n = int(input())
w = input().split()
ans = 0
for s in w:
    if s[-1] == ".":
        s = s[:-1]
    if s in ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]:
        ans += 1
print(ans)
