from collections import defaultdict

h, w, n = map(int, input().split())
indices = defaultdict(list)
r = [0] * 220000
c = [0] * 220000
a = [0] * 220000
for i in range(1, n + 1):
    vr, vc, va = map(int, input().split())
    r[i] = vr
    c[i] = vc
    a[i] = va
    indices[va].append(i)

rmax = [0] * 220000
cmax = [0] * 220000
dp = [0] * 220000

# aが大きい順にdpを解く
# PythonにはC++のmapに相当するデータ構造はない
# 本問ではソートは1度で済むためソートで対応
sorted_keys = sorted(indices.keys(), reverse=True)
for key in sorted_keys:
    # 同じaを持つ要素のdp配列を先に更新する
    for i in indices[key]:
        dp[i] = max(rmax[r[i]], cmax[c[i]])
    # 更新が終わったらrmaxとcmaxを更新する
    # 降順ソートしているため次にrmaxとcmaxを参照するaは必ず今のaより小さい
    for i in indices[key]:
        rmax[r[i]] = max(rmax[r[i]], dp[i] + 1)
        cmax[c[i]] = max(cmax[c[i]], dp[i] + 1)

for i in range(1, n + 1):
    print(dp[i])
