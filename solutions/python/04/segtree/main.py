class SegTree:
    def __init__(self, data):
        n = 1
        while n < len(data):
            n <<= 1
        self.n = n
        self.seg = [0] * (2 * n)
        for i, v in enumerate(data):
            self.seg[n + i] = v
        for i in range(n - 1, 0, -1):
            self.seg[i] = self.seg[2 * i] + self.seg[2 * i + 1]

    def update(self, i, x):
        i += self.n
        self.seg[i] = x
        while i > 1:
            i >>= 1
            self.seg[i] = self.seg[2 * i] + self.seg[2 * i + 1]

    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l & 1:
                res += self.seg[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.seg[r]
            l >>= 1
            r >>= 1
        return res


def main() -> None:
    st = SegTree([1, 2, 3, 4, 5])
    print(st.query(1, 4))
    st.update(2, 10)
    print(st.query(1, 4))


if __name__ == "__main__":
    main()
