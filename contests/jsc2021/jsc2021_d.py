n, p = map(int, input().split())


class Factorial:
    def __init__(self, mod=10 ** 9 + 7):
        self.mod = mod
        self._factorial = [1]
        self._size = 1
        self._factorial_inv = [1]
        self._size_inv = 1

    def __call__(self, n):
        """n! % mod"""
        return self.fact(n)

    def fact(self, n):
        """n! % mod"""
        if n >= self.mod:
            return 0
        self.make(n)
        return self._factorial[n]

    def fact_inv(self, n):
        """n!^-1 % mod"""
        if n >= self.mod:
            raise ValueError("Modinv is not exist! arg={}".format(n))
        self.make_inv(n)
        return self._factorial_inv[n]

    def comb(self, n, r):
        """nCr % mod"""
        if r > n:
            return 0
        t = self.fact_inv(n - r) * self.fact_inv(r) % self.mod
        return self(n) * t % self.mod

    def comb_with_repetition(self, n, r):
        """nHr % mod"""
        t = self.fact_inv(n - 1) * self.fact_inv(r) % self.mod
        return self(n + r - 1) * t % self.mod

    def perm(self, n, r):
        """nPr % mod"""
        if r > n:
            return 0
        return self(n) * self.fact_inv(n - r) % self.mod

    @staticmethod
    def xgcd(a, b):
        """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    def modinv(self, n):
        g, x, _ = self.xgcd(n, self.mod)
        if g != 1:
            raise ValueError("Modinv is not exist! arg={}".format(n))
        return x % self.mod

    def make(self, n):
        if n >= self.mod:
            n = self.mod
        if self._size < n + 1:
            for i in range(self._size, n + 1):
                self._factorial.append(self._factorial[i - 1] * i % self.mod)
            self._size = n + 1

    def make_inv(self, n):
        if n >= self.mod:
            n = self.mod
        self.make(n)
        if self._size_inv < n + 1:
            for i in range(self._size_inv, n + 1):
                self._factorial_inv.append(self.modinv(self._factorial[i]))
            self._size_inv = n + 1


if p < n:
    print(0)
else:
    print(Factorial().perm(p - 1, n - 1))
