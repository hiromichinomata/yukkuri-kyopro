NEG = -(10**30)


class SegBeats:
    """区間 chmin（a[i] = min(a[i], x)）と区間和。閉区間 [l, r]。"""

    def __init__(self, arr):
        n = len(arr)
        self.n = n
        size = 4 * n
        self.sum = [0] * size
        self.mx = [0] * size  # 区間の最大値
        self.se = [0] * size  # 区間の 2 番目に大きい値（最大値より真に小さいもの）
        self.cnt = [0] * size  # 最大値の個数
        self._build(arr, 1, 0, n - 1)

    def _push_up(self, i):
        l, r = i * 2, i * 2 + 1
        self.sum[i] = self.sum[l] + self.sum[r]
        if self.mx[l] == self.mx[r]:
            self.mx[i] = self.mx[l]
            self.cnt[i] = self.cnt[l] + self.cnt[r]
            self.se[i] = max(self.se[l], self.se[r])
        elif self.mx[l] > self.mx[r]:
            self.mx[i] = self.mx[l]
            self.cnt[i] = self.cnt[l]
            self.se[i] = max(self.se[l], self.mx[r])
        else:
            self.mx[i] = self.mx[r]
            self.cnt[i] = self.cnt[r]
            self.se[i] = max(self.mx[l], self.se[r])

    def _build(self, arr, i, l, r):
        if l == r:
            self.sum[i] = self.mx[i] = arr[l]
            self.se[i] = NEG
            self.cnt[i] = 1
            return
        mid = (l + r) // 2
        self._build(arr, i * 2, l, mid)
        self._build(arr, i * 2 + 1, mid + 1, r)
        self._push_up(i)

    def _apply_chmin(self, i, x):
        """se[i] < x < mx[i] のときだけ呼ぶ: 最大値だけが x に下がる"""
        if self.mx[i] <= x:
            return
        self.sum[i] -= (self.mx[i] - x) * self.cnt[i]
        self.mx[i] = x

    def _push_down(self, i):
        # 親の最大値が子より小さくなっていたら、子にも chmin を伝える
        for c in (i * 2, i * 2 + 1):
            self._apply_chmin(c, self.mx[i])

    def range_chmin(self, ql, qr, x, i=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql or self.mx[i] <= x:
            return
        if ql <= l and r <= qr and self.se[i] < x:
            self._apply_chmin(i, x)
            return
        self._push_down(i)
        mid = (l + r) // 2
        self.range_chmin(ql, qr, x, i * 2, l, mid)
        self.range_chmin(ql, qr, x, i * 2 + 1, mid + 1, r)
        self._push_up(i)

    def range_sum(self, ql, qr, i=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.sum[i]
        self._push_down(i)
        mid = (l + r) // 2
        return self.range_sum(ql, qr, i * 2, l, mid) + self.range_sum(ql, qr, i * 2 + 1, mid + 1, r)


def main() -> None:
    arr = [5, 4, 3, 2, 1]
    st = SegBeats(arr)
    print(st.range_sum(0, 4))
    st.range_chmin(1, 3, 2)
    print(st.range_sum(0, 4))
    st.range_chmin(0, 4, 3)
    print(st.range_sum(0, 4), st.range_sum(0, 1))


if __name__ == "__main__":
    main()
