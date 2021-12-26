l, r = map(int, input().split())
l -= 1
s = input()
ans = s[:l] + s[l:r][::-1] + s[r:]
print(ans)
