import re
s=input()
res=0
for i in range(len(s)):
 for j in range(i+1,len(s)+1):
  if re.search(r'[^ACGT]+',s[i:j]):
   pass
  else:
   res=max(res,j-i)
print(res)

"""
インデックスまわりの処置をミスって3回WA取った。
ミスなく実装するにはどう考えるのがよいか要検証。
"""
