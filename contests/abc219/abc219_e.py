class DSU:
	def __init__(self,n):
		self.p=[-1]*n
	def r(self,x):
		if self.p[x]<0:return x
		self.p[x]=self.r(self.p[x])
		return self.p[x]
	def u(self,x,y):
		x=self.r(x)
		y=self.r(y)
		if x==y:return
		if x>y:x,y=y,x
		self.p[x]+=self.p[y]
		self.p[y]=x
	def s(self,x):
		return -self.p[self.r(x)]
	
b=int(''.join(c for c in input()+input()+input()+input() if c!=' ')[::-1],2)
ex=[[0]*6 for _ in range(6)]
ans=0
for i in range(1<<16):
	if i&b!=b:continue
	u=DSU(36)
	s=0
	for j in range(4):
		for k in range(4):
			f=i>>j*4+k&1
			ex[-~j][-~k]=f
			if f:s=-~j*6-~k
	for j in range(6):
		for k in range(6):
			if -~j<6 and ex[j][k]==ex[-~j][k]:u.u(j*6+k,-~j*6+k)
			if -~k<6 and ex[j][k]==ex[j][-~k]:u.u(j*6+k,j*6-~k)
	ans+=u.s(s)+u.s(0)==36
print(ans)