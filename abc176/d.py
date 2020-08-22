h,w=map(int,input().split())
ch,cw=map(int,input().split())
dh,dw=map(int,input().split())
s=[list(str(input())) for _ in range(h)]

def prints():
  for yy in range(h):
    for xx in range(w):
      print(s[yy][xx],end='')
    print()

def dfs(x,y):
  s[x][y]='#'
  prints()
  for i in [-1,1]:
    nx = x+i
    ny = y
    if nx >=0 and nx < w and ny >=0 and ny < h and s[ny][nx]=='.':
      if ny==ch-1 and nx==cw-1:
        return True
      else:
        if dfs(nx,ny):
          return True
  for j in [-1,1]:
      nx = x
      ny = y+j
      if nx >=0 and nx < w and ny >=0 and ny < h and s[ny][nx]=='.':
        if ny==ch-1 and nx==cw-1:
          return True
        else:
          if dfs(nx,ny):
            return True
  return False

res=0

if dfs(dh-1,dw-1):
  print('0')
else:
  print('-1')