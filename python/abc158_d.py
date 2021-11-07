from collections import deque

s = input()
q = int(input())

d = deque()
for c in s:
    d.append(c)

reverse = False
for _ in range(q):
    query = input().split()
    if query[0] == "1":
        reverse = not reverse
    else:
        f, c = query[1:]
        if f == "1":
            if reverse:
                d.append(c)
            else:
                d.appendleft(c)
        else:
            if reverse:
                d.appendleft(c)
            else:
                d.append(c)

ans = "".join(reversed(d) if reverse else d)
print(ans)
