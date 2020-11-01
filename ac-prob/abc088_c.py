c=[[*map(int,input().split())] for _ in range(3)]
row,col=[],[]
for i in range(3):
    row.append([c[i][j]-c[i][0] for j in range(3)])
    col.append([c[j][i]-c[0][i] for j in range(3)])
if row[0]==row[1]==row[2] and col[0]==col[1]==col[2]:
  print('Yes')
else:
  print('No')