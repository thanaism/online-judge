n = int(input())
s = input()
t = ""
for i in s:
    t += i
    if len(t) > 2 and t[-3::] == "fox":
        t = t[:-3]
print(len(t))
