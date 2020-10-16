"""TLE
n,s=input().split()
n=int(n)
l=[[0,0,0,0]]
for i in range(n):
  a=s[0:i+1].count('A')
  g=s[0:i+1].count('G')
  c=s[0:i+1].count('C')
  t=s[0:i+1].count('T')
  l.append([a,g,c,t])
count=0
for i in range(n):
  for j in range(i+1,n+1):
   if i<j and l[j][0]-l[i][0]==l[j][3]-l[i][3] and l[j][1]-l[i][1]==l[j][2]-l[i][2]:
    count+=1
print(count)
"""
# PyPyにしたら通った
n,s=input().split()
n=int(n)
a=[0]
g=[0]
c=[0]
t=[0]
for i in range(n):
  a.append(s[0:i+1].count('A'))
  g.append(s[0:i+1].count('G'))
  c.append(s[0:i+1].count('C'))
  t.append(s[0:i+1].count('T'))
count=0
for i in range(n):
  for j in range(i+1,n+1):
   if all([
    a[j]-a[i]==t[j]-t[i],
    g[j]-g[i]==c[j]-c[i]
   ]):
    count+=1
print(count)