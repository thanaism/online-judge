h,w=map(int,input().split())
si,sj=map(int,input().split())
gi,gj=map(int,input().split())
si-=1;sj-=1
gi-=1;gj-=1
grid=[]
for _ in range(h):
    grid.append(list(input()))
from collections import deque
que=deque()
warp=deque()
que.append([si,sj])
grid[si][sj]=0
di=[-1,0,1,0]
dj=[0,1,0,-1]
while que:
    i,j=que.popleft()
    warp.append([i,j])
    cost=grid[i][j]
    for k in range(4):
        ni=i+di[k]
        nj=j+dj[k]
        if ni<0 or ni>=h:continue
        if nj<0 or nj>=w:continue
        if grid[ni][nj]!='#':
            if grid[ni][nj]=='.':
                que.appendleft([ni,nj])
                grid[ni][nj]=cost 
            elif grid[ni][nj]>cost:
                que.appendleft([ni,nj])
                grid[ni][nj]=cost
    for k in range(-2,3):
        for l in range(-2,3):
            ni=i+k
            nj=j+l
            if ni<0 or ni>=h:continue
            if nj<0 or nj>=w:continue
            if grid[ni][nj]=='.':
                que.append([ni,nj])
                grid[ni][nj]=cost+1
ans=grid[gi][gj]
if ans=='.':ans=-1
print(ans)
