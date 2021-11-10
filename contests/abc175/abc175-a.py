from sys import stdin

S = stdin.readline().rstrip()

count = 0
if S[0] == "R":
    if S[1] == "R":
        if S[2] == "R":
            count = 3
        else:
            count = 2
    else:
        if S[2] == "R":
            count = 1
        else:
            count = 1
else:
    if S[1] == "R":
        if S[2] == "R":
            count = 2
        else:
            count = 1
    else:
        if S[2] == "R":
            count = 1
        else:
            count = 0

print(count)
