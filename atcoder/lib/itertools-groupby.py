# abc175_aに使用例あり
from itertools import groupby
mylist = [0,0,0,1,1,2,2,2,1,1,1]
for key, group in groupby(mylist):
  print(key, list(group))

# 出力
# 0 [0, 0, 0]
# 1 [1, 1]
# 2 [2, 2, 2]
# 1 [1, 1, 1]