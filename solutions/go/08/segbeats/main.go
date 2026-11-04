package main

import "fmt"

const neg = -1 << 60

// segBeats は区間 chmin（a[i] = min(a[i], x)）と区間和。閉区間 [l, r]。
type segBeats struct {
	n           int
	sum, mx, se []int // mx: 最大値, se: 2 番目に大きい値（最大値より真に小さいもの）
	cnt         []int // 最大値の個数
}

func newSegBeats(arr []int) *segBeats {
	n := len(arr)
	s := &segBeats{n: n}
	s.sum = make([]int, 4*n)
	s.mx = make([]int, 4*n)
	s.se = make([]int, 4*n)
	s.cnt = make([]int, 4*n)
	s.build(arr, 1, 0, n-1)
	return s
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func (s *segBeats) pushUp(i int) {
	l, r := i*2, i*2+1
	s.sum[i] = s.sum[l] + s.sum[r]
	switch {
	case s.mx[l] == s.mx[r]:
		s.mx[i], s.cnt[i], s.se[i] = s.mx[l], s.cnt[l]+s.cnt[r], max(s.se[l], s.se[r])
	case s.mx[l] > s.mx[r]:
		s.mx[i], s.cnt[i], s.se[i] = s.mx[l], s.cnt[l], max(s.se[l], s.mx[r])
	default:
		s.mx[i], s.cnt[i], s.se[i] = s.mx[r], s.cnt[r], max(s.mx[l], s.se[r])
	}
}

func (s *segBeats) build(arr []int, i, l, r int) {
	if l == r {
		s.sum[i], s.mx[i], s.cnt[i], s.se[i] = arr[l], arr[l], 1, neg
		return
	}
	mid := (l + r) / 2
	s.build(arr, i*2, l, mid)
	s.build(arr, i*2+1, mid+1, r)
	s.pushUp(i)
}

// applyChmin は se[i] < x < mx[i] のときだけ呼ぶ: 最大値だけが x に下がる
func (s *segBeats) applyChmin(i, x int) {
	if s.mx[i] <= x {
		return
	}
	s.sum[i] -= (s.mx[i] - x) * s.cnt[i]
	s.mx[i] = x
}

// pushDown: 親の最大値が子より小さくなっていたら、子にも chmin を伝える
func (s *segBeats) pushDown(i int) {
	s.applyChmin(i*2, s.mx[i])
	s.applyChmin(i*2+1, s.mx[i])
}

func (s *segBeats) RangeChmin(ql, qr, x int) { s.rangeChmin(ql, qr, x, 1, 0, s.n-1) }

func (s *segBeats) rangeChmin(ql, qr, x, i, l, r int) {
	if qr < l || r < ql || s.mx[i] <= x {
		return
	}
	if ql <= l && r <= qr && s.se[i] < x {
		s.applyChmin(i, x)
		return
	}
	s.pushDown(i)
	mid := (l + r) / 2
	s.rangeChmin(ql, qr, x, i*2, l, mid)
	s.rangeChmin(ql, qr, x, i*2+1, mid+1, r)
	s.pushUp(i)
}

func (s *segBeats) RangeSum(ql, qr int) int { return s.rangeSum(ql, qr, 1, 0, s.n-1) }

func (s *segBeats) rangeSum(ql, qr, i, l, r int) int {
	if qr < l || r < ql {
		return 0
	}
	if ql <= l && r <= qr {
		return s.sum[i]
	}
	s.pushDown(i)
	mid := (l + r) / 2
	return s.rangeSum(ql, qr, i*2, l, mid) + s.rangeSum(ql, qr, i*2+1, mid+1, r)
}

func main() {
	st := newSegBeats([]int{5, 4, 3, 2, 1})
	fmt.Println(st.RangeSum(0, 4))
	st.RangeChmin(1, 3, 2)
	fmt.Println(st.RangeSum(0, 4))
	st.RangeChmin(0, 4, 3)
	fmt.Println(st.RangeSum(0, 4), st.RangeSum(0, 1))
}
