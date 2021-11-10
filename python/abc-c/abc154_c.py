n = int(input())
a = [*map(int, input().split())]
from collections import Counter

if Counter(a).most_common()[0][1] == 1:
    print("YES")
else:
    print("NO")
