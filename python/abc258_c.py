from collections import deque

n, q = map(int, input().split())
s = input()

offset = -1

for _ in range(q):
    a, x = map(int, input().split())
    if a == 1:
        offset -= x
    if a == 2:
        i = (x + offset) % n
        print(s[i])
