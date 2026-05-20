package main

import "fmt"

type SegTree struct {
	n   int
	seg []int
}

func NewSegTree(data []int) *SegTree {
	n := 1
	for n < len(data) {
		n <<= 1
	}
	seg := make([]int, 2*n)
	for i, v := range data {
		seg[n+i] = v
	}
	for i := n - 1; i > 0; i-- {
		seg[i] = seg[2*i] + seg[2*i+1]
	}
	return &SegTree{n, seg}
}

func (s *SegTree) Update(i, x int) {
	i += s.n
	s.seg[i] = x
	for i > 1 {
		i >>= 1
		s.seg[i] = s.seg[2*i] + s.seg[2*i+1]
	}
}

func (s *SegTree) Query(l, r int) int {
	l += s.n
	r += s.n
	res := 0
	for l < r {
		if l&1 == 1 {
			res += s.seg[l]
			l++
		}
		if r&1 == 1 {
			r--
			res += s.seg[r]
		}
		l >>= 1
		r >>= 1
	}
	return res
}

func main() {
	st := NewSegTree([]int{1, 2, 3, 4, 5})
	fmt.Println(st.Query(1, 4))
	st.Update(2, 10)
	fmt.Println(st.Query(1, 4))
}
