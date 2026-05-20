package main

import "fmt"

type LazySeg struct {
	n, size int
	seg     []int64
	lazy    []int64
}

func NewLazySeg(data []int) *LazySeg {
	size := 1
	for size < len(data) {
		size <<= 1
	}
	seg := make([]int64, 2*size)
	lazy := make([]int64, 2*size)
	for i, v := range data {
		seg[size+i] = int64(v)
	}
	return &LazySeg{len(data), size, seg, lazy}
}

func (t *LazySeg) apply(i, l, r int, x int64) {
	t.seg[i] += x * int64(r-l)
	t.lazy[i] += x
}

func (t *LazySeg) push(i, l, r int) {
	if t.lazy[i] == 0 || i >= t.size {
		return
	}
	m := (l + r) / 2
	x := t.lazy[i]
	t.apply(2*i, l, m, x)
	t.apply(2*i+1, m, r, x)
	t.lazy[i] = 0
}

func (t *LazySeg) pull(i int) {
	t.seg[i] = t.seg[2*i] + t.seg[2*i+1]
}

func (t *LazySeg) RangeAdd(ql, qr int, x int64) {
	t.rangeAdd(ql, qr, x, 1, 0, t.size)
}

func (t *LazySeg) rangeAdd(ql, qr int, x int64, i, l, r int) {
	if qr <= l || r <= ql {
		return
	}
	if ql <= l && r <= qr {
		t.apply(i, l, r, x)
		return
	}
	t.push(i, l, r)
	m := (l + r) / 2
	t.rangeAdd(ql, qr, x, 2*i, l, m)
	t.rangeAdd(ql, qr, x, 2*i+1, m, r)
	t.push(2*i, l, m)
	t.push(2*i+1, m, r)
	t.pull(i)
}

func (t *LazySeg) RangeSum(ql, qr int) int64 {
	return t.rangeSum(ql, qr, 1, 0, t.size)
}

func (t *LazySeg) rangeSum(ql, qr, i, l, r int) int64 {
	if qr <= l || r <= ql {
		return 0
	}
	if ql <= l && r <= qr {
		return t.seg[i]
	}
	t.push(i, l, r)
	m := (l + r) / 2
	return t.rangeSum(ql, qr, 2*i, l, m) + t.rangeSum(ql, qr, 2*i+1, m, r)
}

func main() {
	st := NewLazySeg(make([]int, 8))
	st.RangeAdd(1, 5, 10)
	st.RangeAdd(3, 7, 5)
	fmt.Println(st.RangeSum(0, 8))
}
