from typing import Sequence


n, k = map(int, input().split())
at = [0] * 1500
score = []
for _ in range(n):
    p = sum([*map(int, input().split())])
    at[p] += 1
    score.append(p + 300)

for i in range(1, 1500):
    at[i] += at[i - 1]

for i in score:
    if at[i] + k > n:
        print("Yes")
    else:
        print("No")
