class SegBeats:
    def __init__(self, arr):
        n = len(arr)
        self.n = n
        size = 4 * n
        self.sum = [0] * size
        self.mx = [0] * size
        self.se = [0] * size
        self.cnt = [0] * size
        self._build(arr, 1, 0, n - 1)

    def _push_up(self, i):
        l, r = i * 2, i * 2 + 1
        self.sum[i] = self.sum[l] + self.sum[r]
        if self.mx[l] >= self.mx[r]:
            self.mx[i] = self.mx[l]
            self.cnt[i] = self.cnt[l]
            self.se[i] = self.se[l]
            if self.mx[r] > self.se[i]:
                self.se[i] = self.mx[r]
        else:
            self.mx[i] = self.mx[r]
            self.cnt[i] = self.cnt[r]
            self.se[i] = self.se[r]
            if self.mx[l] > self.se[i]:
                self.se[i] = self.mx[l]

    def _build(self, arr, i, l, r):
        if l == r:
            self.sum[i] = self.mx[i] = arr[l]
            self.se[i] = -10**30
            self.cnt[i] = 1
            return
        mid = (l + r) // 2
        self._build(arr, i * 2, l, mid)
        self._build(arr, i * 2 + 1, mid + 1, r)
        self._push_up(i)

    def _apply_chmin(self, i, x):
        if self.mx[i] <= x:
            return
        self.sum[i] -= (self.mx[i] - x) * self.cnt[i]
        self.mx[i] = x

    def range_chmin(self, ql, qr, x, i=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql or self.mx[i] <= x:
            return
        if ql <= l and r <= qr and self.se[i] < x:
            self._apply_chmin(i, x)
            return
        self.range_chmin(ql, qr, x, i * 2, l, (l + r) // 2)
        self.range_chmin(ql, qr, x, i * 2 + 1, (l + r) // 2 + 1, r)
        self._push_up(i)

    def range_sum(self, ql, qr, i=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.sum[i]
        mid = (l + r) // 2
        return self.range_sum(ql, qr, i * 2, l, mid) + self.range_sum(
            ql, qr, i * 2 + 1, mid + 1, r
        )


def main() -> None:
    arr = [5, 4, 3, 2, 1]
    st = SegBeats(arr)
    print(st.range_sum(0, 4))
    st.range_chmin(1, 3, 2)
    print(st.range_sum(0, 4))


if __name__ == "__main__":
    main()
