n=int(input())
ans=0
mat=[]
for _ in range(n):
    mat.append([*map(int,input().split())])
for i in range(n):
    for j in range(i+1,n):
        a=mat[i]
        b=mat[j]
        dx=a[0]-b[0]
        dy=a[1]-b[1]
        if abs(dy/dx)<=1:ans+=1
print(ans)    