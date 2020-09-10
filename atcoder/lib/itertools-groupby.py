# ABC175-A
from itertools import groupby
mylist = [0,0,0,1,1,2,2,2,1,1,1]
for key, group in groupby(mylist):
  print(key, list(group),type(group))

# s = input()
# if s == 'RRR':
#   res = 3
# elif s =='SRR':
#   res = 2
# elif s =='RSR':
#   res = 1
# elif s =='RRS':
#   res = 2
# elif s =='RSS':
#   res = 1
# elif s =='SRS':
#   res = 1
# elif s =='SSR':
#   res = 1
# else:
#   res = 0
# print(res)

# s = input()
# if 'RRR' in s:
#     res = 3
# elif 'RR' in s:
#     res = 2
# elif 'R' in s:
#     res = 1
# else:
#     res = 0
# print(res)