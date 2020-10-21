"""h,w=map(int,input().split())
a=[]
for i in range(h):
  a.append([j for j in input()])
res=[]
for i in range(h):
  if '#' in a[i]:
    res.append(a[i])
ignore=set()
for j in range(w):
  ok=True
  for i in range(len(res)):
    if res[i][j]=='#':
      ok=False
  if ok:
    ignore|={j}
for i in range(len(res)):
  for j in range(w-1,-1,-1):
    if j in ignore:
      del res[i][j]
for i in res:
  print(''.join(i))"""

  # ACは取れたが、実際に配列を要素削除する必要はなかった
  # 黒いマスがある行列のインデックスにフラグを立て、
  # フラグの立っている行列のみ出力するほうがスマート
h,w=map(int,input().split())
a=[input() for _ in range(h)]
row=set()
col=set()
for i in range(h):
  for j in range(w):
    if a[i][j]=='#':
      row|={i}
      col|={j}
for i in range(h):
  if i in row:
    for j in range(w):
      if j in col:
        print(a[i][j],end='')
    print()