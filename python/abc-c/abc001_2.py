m = int(input())
if m < 100:
    vv = 0
elif 100 <= m <= 5000:
    vv = m // 100
elif 6000 <= m <= 30000:
    vv = m // 1000 + 50
elif 35000 <= m <= 70000:
    vv = (m - 30000) // 5000 + 80
elif 70000 < m:
    vv = 89
print(f"{vv:02d}")
