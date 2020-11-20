x,y=map(int,input().split())
a=0
while a*2+(x-a)*4!=y:
    a+=1
    if a>x:break
print('Yes' if a<=x else 'No')
