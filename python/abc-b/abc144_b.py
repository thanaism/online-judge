n = int(input())
l = [i * j for i in range(1, 10) for j in range(1, 10)]
print("Yes" if n in l else "No")
