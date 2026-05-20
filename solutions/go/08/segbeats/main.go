package main

import "fmt"

type segBeats struct {
	n, size      int
	sum, mx, se  []int
	cnt          []int
}

func newSegBeats(arr []int) *segBeats {
	n := len(arr)
	s := &segBeats{n: n, size: 4 * n}
	s.sum = make([]int, s.size)
	s.mx = make([]int, s.size)
	s.se = make([]int, s.size)
	s.cnt = make([]int, s.size)
	s.build(arr, 1, 0, n-1)
	return s
}

func (s *segBeats) pushUp(i int) {
	l, r := i*2, i*2+1
	s.sum[i] = s.sum[l] + s.sum[r]
	if s.mx[l] >= s.mx[r] {
		s.mx[i], s.cnt[i], s.se[i] = s.mx[l], s.cnt[l], s.se[l]
		if s.mx[r] > s.se[i] {
			s.se[i] = s.mx[r]
		}
	} else {
		s.mx[i], s.cnt[i], s.se[i] = s.mx[r], s.cnt[r], s.se[r]
		if s.mx[l] > s.se[i] {
			s.se[i] = s.mx[l]
		}
	}
}

func (s *segBeats) build(arr []int, i, l, r int) {
	if l == r {
		s.sum[i], s.mx[i], s.cnt[i] = arr[l], arr[l], 1
		s.se[i] = -1_000_000_000
		return
	}
	mid := (l + r) / 2
	s.build(arr, i*2, l, mid)
	s.build(arr, i*2+1, mid+1, r)
	s.pushUp(i)
}

func (s *segBeats) applyChmin(i, x int) {
	if s.mx[i] <= x {
		return
	}
	s.sum[i] -= (s.mx[i] - x) * s.cnt[i]
	s.mx[i] = x
}

func (s *segBeats) rangeChmin(ql, qr, x, i, l, r int) {
	if qr < l || r < ql || s.mx[i] <= x {
		return
	}
	if ql <= l && r <= qr && s.se[i] < x {
		s.applyChmin(i, x)
		return
	}
	mid := (l + r) / 2
	s.rangeChmin(ql, qr, x, i*2, l, mid)
	s.rangeChmin(ql, qr, x, i*2+1, mid+1, r)
	s.pushUp(i)
}

func (s *segBeats) rangeSum(ql, qr, i, l, r int) int {
	if qr < l || r < ql {
		return 0
	}
	if ql <= l && r <= qr {
		return s.sum[i]
	}
	mid := (l + r) / 2
	return s.rangeSum(ql, qr, i*2, l, mid) + s.rangeSum(ql, qr, i*2+1, mid+1, r)
}

func main() {
	arr := []int{5, 4, 3, 2, 1}
	st := newSegBeats(arr)
	fmt.Println(st.rangeSum(0, 4, 1, 0, 4))
	st.rangeChmin(1, 3, 2, 1, 0, 4)
	fmt.Println(st.rangeSum(0, 4, 1, 0, 4))
}
