"""
n=int(input())
s=[]
for _ in range(n):
  s.append(input())
memo=[]

def remove(d,i):
  for j,v in enumerate(s[i]):
    if (j not in d) and v=='1':
      d|={j}
      remove(d,j)

def dfs(deleted,cnt):
  if len(deleted)==n:
    memo.append(cnt)
    return
  for i,v in enumerate(s):
    if i not in deleted:
      d=deleted.copy()
      d|={i}
      remove(d,i)
      dfs(d,cnt+1)
dfs(set(),0)
print(sum(memo)/len(memo))
"""

# 入力
n = int(input())
s = [input() for _ in range(n)]
# 出力の初期化
ans = 0
# 全頂点に関してループ
for i in range(n):
    # 頂点をキューに追加する
    que = [i]
    # 削除済かのフラグ
    deleted = [False] * n
    # キューが空になるまでループ
    while que:
        # キューから頂点を取り出し
        v = que.pop()
        # 削除済なら次の頂点へ
        if deleted[v]:
            continue
        # 削除済フラグを立てる
        deleted[v] = True
        # 頂点vから頂点uに辺があるかチェック
        for u in range(n):
            # 削除済または辺がない場合は次へ
            if deleted[u] or s[u][v] == "0":
                continue
            # 未削除の辺があれば頂点uをキューに追加
            que.append(u)
    # 頂点vから到達可能な全頂点の逆数を加える
    ans += 1 / sum(deleted)
# 出力
print(ans)
