class MonoidSeg:
    def __init__(self, data, op, e):
        self.n = len(data)
        self.op = op
        self.e = e
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.dat = [e] * (2 * size)
        for i, x in enumerate(data):
            self.dat[size + i] = x
        for i in range(size - 1, 0, -1):
            self.dat[i] = op(self.dat[i * 2], self.dat[i * 2 + 1])

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 1:
            i //= 2
            self.dat[i] = self.op(self.dat[i * 2], self.dat[i * 2 + 1])

    def query(self, l, r):
        l += self.size
        r += self.size
        left = right = self.e
        while l < r:
            if l & 1:
                left = self.op(left, self.dat[l])
                l += 1
            if r & 1:
                r -= 1
                right = self.op(self.dat[r], right)
            l //= 2
            r //= 2
        return self.op(left, right)


def main() -> None:
    data = [1, 3, 2, 5, 4]
    mx = MonoidSeg(data, max, -10**30)
    sm = MonoidSeg(data, lambda a, b: a + b, 0)
    print(mx.query(1, 4))
    print(sm.query(0, 5))
    mx.update(2, 10)
    print(mx.query(0, 5))


if __name__ == "__main__":
    main()
