from itertools import permutations


class Grid:
    """
    各点に左上から0-indexedな番号を振る
    ex) 3x3の場合
    0 1 2
    3 4 5
    6 7 8
    """

    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.row = lambda i: i // self.col_size
        self.col = lambda i: i % self.col_size
        self.pos = lambda i: (self.row(i), self.col(i))
        self.n = row_size * col_size
        self.between = [[[] for _ in range(self.n)] for _ in range(self.n)]
        # 2点(i,j)を結ぶ直線状にある点(k)をリスト化する
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if k == i or k == j:
                        continue
                    if self.is_between(k, i, j):
                        self.between[i][j].append(k)

    def is_between(self, k, i, j):
        """点(k)が点(i,j)の間にあるかを返す"""
        # a = self.pos(i)
        # b = self.pos(j)
        # c = self.pos(k)
        a, b, c = map(self.pos, (i, j, k))
        return (
            self.squared_distance(a, b) > self.squared_distance(a, c)
            and self.squared_distance(a, b) > self.squared_distance(b, c)
            and self.is_collinear(a, b, c)
        )

    def squared_distance(self, a, b):
        """2点間の距離の2乗を返す"""
        return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

    def is_collinear(self, a, b, c):
        """3点が同一直線状にあるかを返す"""
        return (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0]) == 0


def main():
    row_size, col_size, pattern_length = map(int, input().split())
    n = row_size * col_size

    g = Grid(row_size, col_size)

    ans = 0
    for p in permutations(range(n), pattern_length):
        used = set()
        ok = True
        for i in range(pattern_length - 1):
            pre = p[i]
            nxt = p[i + 1]
            for mid in g.between[pre][nxt]:
                if mid not in used:
                    ok = False
            if not ok:
                break
            used.add(pre)
        if ok:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
