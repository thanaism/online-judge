"""
h,w=map(int,input().split())
s=[]
for _ in range(h):
 s.append(input())
yet=[[True]*w for _ in range(h)]
count=0
for i in range(h):
 for j in range(w):
  yet[i][j]=False
  if s[i][j]=='.':
   #top
   if i!=0:
    if s[i-1][j]=='.' and yet[i-1][j]:
     count+=1
     # yet[i-1][j]=False
   #right
   if j!=w-1:
    if s[i][j+1]=='.' and yet[i][j+1]:
     count+=1
     # yet[i][j+1]=False
   #left
   if j!=0:
    if s[i][j-1]=='.' and yet[i][j-1]:
     count+=1
     # yet[i][j-1]=False
   #down
   if i!=h-1:
    if s[i+1][j]=='.' and yet[i+1][j]:
     count+=1
     # yet[i+1][j]=False
print(count)
"""


h,w=map(int,input().split())
s=[]
for _ in range(h):
 s.append(input())
yet=[[True]*w for _ in range(h)]
count=0
for i in range(h):
 for j in range(w):
  yet[i][j]=False
  if s[i][j]=='.':
   #right
   if j!=w-1:
    if s[i][j+1]=='.':
     count+=1
   #down
   if i!=h-1:
    if s[i+1][j]=='.':
     count+=1
print(count)
