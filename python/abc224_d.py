# 辺の個数
m = int(input())

# 隣接行列：uとvの間に辺があればTrue
edges = [[False] * 10 for _ in range(10)]
for _ in range(m):
    u, v = map(int, input().split())
    edges[u][v] = True
    edges[v][u] = True

# p：i番目の数字がどの位置にいるか
p = input().split()
# どの数字も置かれていない場所が"9"の位置
for i in range(1, 10):
    if str(i) not in p:
        p.append(str(i))
        break

# pは辞書のkeyとなるため高速化を考慮して整数にする
# 0を含まないのでleading zeroは考慮不要
p = int(''.join(p))

vec = [p]  # 探索の起点を格納：初期状態
dist = {p: 0}  # 各状態へ遷移するための最小の操作回数

# キューを使用しない形式のBFS
while vec:
    new_vec = []  # 探索過程で見つけた次の深さのノードを格納するリスト
    # 現在の深さのノードを順に探索する
    for p in vec:
        now = list(str(p))  # Pythonの文字列はsubscriptableでないので文字のリストに変換する
        nine = int(now[8])  # 9＝空ノードの現在位置
        for i in range(8):
            pos = int(now[i])  # 今見ている数字iの現在位置
            if edges[pos][nine]:  # 今見ている数字iと9が連結ならば
                now[i], now[8] = now[8], now[i]  # 位置を交換する
                nxt = int(''.join(now))  # 交換後の状態を辞書のkeyとするため整数に変換
                if nxt not in dist:  # 訪問したことがないなら
                    dist[nxt] = dist[p] + 1  # 1回操作を加えればnowからnxtの状態にできる
                    new_vec.append(nxt)  # 次の深さの探索先リストに加える
                now[i], now[8] = now[8], now[i]  # swapしたものを元に戻す
    vec = new_vec  # 現在の深さの探索が終了したので探索先のリストを次の深さのもので置き換える

# 探索の終了時点で9!通りのうち、実現可能な状態がすべてdistに格納されている
goal = 123456789  # 今回期待する状態
if goal in dist:
    print(dist[goal])
else:
    print(-1)
