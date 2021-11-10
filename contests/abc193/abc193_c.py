from math import log

n = int(input())
ans = n
s = set()
for i in range(1, n):
    if i * i > n:
        break
    if i < 2:
        continue
    # print(i,((log(n)+log(i)-1)//log(i)))
    for j in range(2, int(log(n) // log(i)) + 2):
        if i ** j <= n:
            s |= {i ** j}
            # print(i,j)
print(n - len(s))
