class CumulativeSum2D:
    def __init__(self, h, w):
        self.h = h + 1
        self.w = w + 1
        self.table = [[0] * self.w for _ in range(self.h)]

    def add(self, i, j, x):
        self.table[i + 1][j + 1] += x

    def build(self):
        for i in range(self.h):
            for j in range(self.w):
                if i:
                    self.table[i][j] += self.table[i - 1][j]
        for i in range(self.h):
            for j in range(self.w):
                if j:
                    self.table[i][j] += self.table[i][j - 1]

    def get(self, i1, j1, i2, j2):
        return (
            self.table[i2][j2]
            - self.table[i2][j1]
            - self.table[i1][j2]
            + self.table[i1][j1]
        )


def is_ok(x):
    cs = CumulativeSum2D(n, n)
    for i in range(n):
        for j in range(n):
            if a[i][j] > x:
                cs.add(i, j, 1)

    cs.build()
    limit = k * k // 2 + 1

    for i in range(n - k + 1):
        for j in range(n - k + 1):
            if cs.get(i, j, i + k, j + k) < limit:
                return True

    return False


def main():
    ok = max([max(line) for line in a])
    ng = -1
    while (ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = [[*map(int, input().split())] for _ in range(n)]
    main()
