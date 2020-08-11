from sys import stdin
N = int(stdin.readline().rstrip())
c = stdin.readline().rstrip()
R_cnt = c.count('R')
L_cnt = 0
for i in range(R_cnt):
  if c[i] == 'R':
    L_cnt += 1
print(R_cnt - L_cnt)