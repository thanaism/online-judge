h,w=map(int,input().split())
grid=[]
for _ in range(h):
    grid.append(input())
ans=0
for i in range(1,h):
    for j in range(1,w):
        c=0
        for ii in [i,i-1]:
            for jj in [j,j-1]:
                if grid[ii][jj]=='#':c+=1
        if c&1:
            ans+=1
print(ans)
# from collections import deque
# di=[-1,0,1,0]
# dj=[0,1,0,-1]
# ans=0
# done=set()
# for i in range(1,h-1):
#     for j in range(1,w-1):
#         if grid[i][j]=='.':continue
#         q=deque()
#         q.append((i,j))
#         while q:
#             ii,jj=q.popleft()
#             done|={(ii,jj)}
#             count=0
#             for k in range(4):
#                 ni=ii+di[k]
#                 nj=jj+dj[k]
#                 if grid[ni][nj]=='#':
#                     if (ni,nj) not in done:
#                         q.append((ni,nj))
#                 else:
#                     count+=1
#             if count==2:ans+=1
#             if count==3:ans+=2
# print(ans-2)