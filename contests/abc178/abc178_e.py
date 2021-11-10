"""
m,p=[],[]
for i in [*open(0)][1:]:
  x,y=map(int,i.split())
  m.append(x-y)
  p.append(x+y)
f=lambda x:max(x)-min(x)
print(max(f(m),f(p)))
"""

m, *p = ([],)
for i in [*open(0)][1:]:
    x, y = map(int, i.split())
    m += (x - y,)
    p += (x + y,)
a = max
print(a(a(m) - min(m), a(p) - min(p)))
