x,y,a,b=map(int,input().split())
EXP=0
STR=x

def search(s,e):
  return e+(y-s-1)//b
 
res=0
while STR<y and STR<=x+b:
  EXP+=1
  STR*=a
  res=max(res,search(STR,EXP))
print(res)