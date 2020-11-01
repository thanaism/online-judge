n=int(input())
s=set()
for _ in range(n):
  i=input()
  if i in s:
    s.remove(i)
  else:
    s|={i}
print(len(s))