n, m = map(int, input().split())
# グラフとコスト記録
g = [list() for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    g[u - 1].append((v - 1, c))
    g[v - 1].append((u - 1, c))

# 頂点を入れるキュー
from collections import deque

que = deque()
# 頂点に書き込む整数
digit = [0] * n
# 頂点を選び1を書き込んだ状態からスタート
que.append(0)
digit[0] = 1
# キューが空になるまで木をBFS
while que:
    # 親を取り出す
    i = que.popleft()
    # 親の数字は常に先に決まっているので取り出す
    p = digit[i]
    # 隣接する頂点をループ
    for v, c in g[i]:
        # 訪問済ならスキップ
        if digit[v] != 0:
            continue
        # 未訪問の場合はキューに追加し次の親とする
        que.append(v)
        if c == p:
            # 辺の数字が親に一致する場合はそれ以外を
            digit[v] = p + 1 if p < n else p - 1
        else:
            # 親と一致しなければ辺の数字を
            digit[v] = c
# 訪れたことのない頂点がある場合は全域木は形成できない
# 今回の問題は連結グラフなので必ず全域木を形成できるはず？
if digit.count(0):
    print("No")
    exit()
for i in digit:
    print(i)
