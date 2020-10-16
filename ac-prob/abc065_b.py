n=int(input())
ls=[int(input())-1 for i in range(n)]
def search():
  pushed=[False]*n
  count=i=0
  while True:
    if pushed[i]:
      return -1
    else:
      pushed[i]=True
      i=ls[i]
      count+=1
      if i==1:
        return count
print(search())
