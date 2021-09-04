s=set()
for _ in range(3):
	s.add(input())
t=set(['ABC','ARC','AGC','AHC'])
print(list(t-s)[0])
