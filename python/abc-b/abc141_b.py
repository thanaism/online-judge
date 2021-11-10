s = input()
ans = "No"
if set("RUD").issuperset(set(s[0::2])) and set("LUD").issuperset(set(s[1::2])):
    ans = "Yes"
print(ans)
