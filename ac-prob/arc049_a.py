s=input()
a,b,c,d=map(int,input().split())
for i in [d,c,b,a]:
  s=s[:i]+'"'+s[i:]
print(s)