a = [list(map(int,input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]
for k in range(n):
  for i in range(3):
    for j in range(3):
      if a[i][j]==b[k]:
        a[i][j]=-1
def result():
  for i in range(3):
    if a[i][0]==a[i][1]==a[i][2]==-1 or a[0][i]==a[1][i]==a[2][i]==-1:
      return 'Yes'
  if a[0][0]==a[1][1]==a[2][2]==-1 or a[0][2]==a[1][1]==a[2][0]==-1:
    return 'Yes'
  else:
    return 'No'
print(result())