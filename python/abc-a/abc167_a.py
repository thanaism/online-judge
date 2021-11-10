f = input
print("YNeos"[f() != f()[:-1] :: 2])
