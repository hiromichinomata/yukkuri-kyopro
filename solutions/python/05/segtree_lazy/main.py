class LazySegTree:
    """区間加算・区間和（サイズは 2 の冪）"""

    def __init__(self, data: list) -> None:
        n = 1
        while n < len(data):
            n <<= 1
        self.n = n
        self.seg = [0] * (2 * n)
        self.lazy = [0] * (2 * n)
        for i, v in enumerate(data):
            self.seg[n + i] = v

    def _apply(self, i: int, l: int, r: int, x: int) -> None:
        self.seg[i] += x * (r - l)
        self.lazy[i] += x

    def _push(self, i: int, l: int, r: int) -> None:
        if self.lazy[i] == 0 or i >= self.n:
            return
        m = (l + r) // 2
        x = self.lazy[i]
        self._apply(2 * i, l, m, x)
        self._apply(2 * i + 1, m, r, x)
        self.lazy[i] = 0

    def _pull(self, i: int) -> None:
        self.seg[i] = self.seg[2 * i] + self.seg[2 * i + 1]

    def range_add(self, ql: int, qr: int, x: int, i: int = 1, l: int = 0, r: int | None = None) -> None:
        if r is None:
            r = self.n
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            self._apply(i, l, r, x)
            return
        self._push(i, l, r)
        m = (l + r) // 2
        self.range_add(ql, qr, x, 2 * i, l, m)
        self.range_add(ql, qr, x, 2 * i + 1, m, r)
        self._push(2 * i, l, m)
        self._push(2 * i + 1, m, r)
        self._pull(i)

    def range_sum(self, ql: int, qr: int, i: int = 1, l: int = 0, r: int | None = None) -> int:
        if r is None:
            r = self.n
        if qr <= l or r <= ql:
            return 0
        if ql <= l and r <= qr:
            return self.seg[i]
        self._push(i, l, r)
        m = (l + r) // 2
        return self.range_sum(ql, qr, 2 * i, l, m) + self.range_sum(ql, qr, 2 * i + 1, m, r)


def main() -> None:
    st = LazySegTree([0] * 8)
    st.range_add(1, 5, 10)
    st.range_add(3, 7, 5)
    print(st.range_sum(0, 8))


if __name__ == "__main__":
    main()
