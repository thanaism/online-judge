n,m=map(int,input().split())
p=[]
for _ in range(n):
  p.append(list(map(int,input().split())))
q=[]
for _ in range(m):
  q.append(list(map(int,input().split())))
for i in range(n):
  nearest=None
  dist=1<<60
  for j in range(m):
    if abs(p[i][0]-q[j][0])+abs(p[i][1]-q[j][1])<dist:
      dist=abs(p[i][0]-q[j][0])+abs(p[i][1]-q[j][1])
      nearest=j+1
  print(nearest)