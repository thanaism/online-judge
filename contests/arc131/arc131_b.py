h, w = map(int, input().split())
color = []
for _ in range(h):
    line = list(input())
    color.append(line)

# for line in color:
#     print(line)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
all = set(["1", "2", "3", "4", "5"])
for i in range(h):
    for j in range(w):
        if color[i][j] != ".":
            continue
        st = set()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if color[ni][nj] == ".":
                continue
            st.add(color[ni][nj])
        res = list(all - st)[0]
        color[i][j] = res

for line in color:
    print("".join(line))
