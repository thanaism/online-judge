"""
s=input()
t=input()
if s=='Y':
 if t=='a':
  print('A')
 elif t=='b':
  print('B')
 elif t=='c':
  print('C')
else:
 print(t)
"""
s = input()
t = input()
print([t, t.upper()][s == "Y"])
