n = int(input())
s = input()
l = [chr(i) for i in range(65, 91)] * 2
ans = ""
for i in s:
    ans += l[ord(i) - 65 + n]
print(ans)
