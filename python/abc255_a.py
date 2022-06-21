r, c = map(int, input().split())
a11, a12 = map(int, input().split())
a21, a22 = map(int, input().split())
p = [[a11, a12], [a21, a22]]
print(p[r - 1][c - 1])
