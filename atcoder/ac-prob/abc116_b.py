s=int(input())
l={s}
m=2
while True:
 if s%2==0:
  s=int(s/2)
 else:
  s=3*s+1
 if s not in l:
  l|={s}
  m+=1
 else:
  print(m)
  break

"""
初項を入れ忘れるというミスを犯して3WA。
境界条件の確認を怠らないこと。
"""