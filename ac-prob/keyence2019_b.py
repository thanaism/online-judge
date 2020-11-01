s=input()
k='keyence'
for i in range(7):
  if k[:i]==s[:i] and k[i-7:]==s[i-7:]:
    print('YES');exit()
print('NO')