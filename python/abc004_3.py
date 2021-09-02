n = int(input())
n %= 30
l = list(map(str,range(1,7)))
for i in range(n):
	j = i%5
	k = j+1
	l[j],l[k] = l[k],l[j]
print(''.join(l))