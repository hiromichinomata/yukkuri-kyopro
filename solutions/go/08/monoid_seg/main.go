package main

import "fmt"

type monoidSeg struct {
	size int
	dat  []int
	op   func(int, int) int
	e    int
}

func newMonoidSeg(data []int, op func(int, int) int, e int) *monoidSeg {
	n := len(data)
	size := 1
	for size < n {
		size <<= 1
	}
	s := &monoidSeg{size: size, op: op, e: e, dat: make([]int, 2*size)}
	for i, x := range data {
		s.dat[size+i] = x
	}
	for i := size - 1; i > 0; i-- {
		s.dat[i] = op(s.dat[i*2], s.dat[i*2+1])
	}
	return s
}

func (s *monoidSeg) query(l, r int) int {
	l += s.size
	r += s.size
	left, right := s.e, s.e
	for l < r {
		if l&1 == 1 {
			left = s.op(left, s.dat[l])
			l++
		}
		if r&1 == 1 {
			r--
			right = s.op(s.dat[r], right)
		}
		l >>= 1
		r >>= 1
	}
	return s.op(left, right)
}

func main() {
	data := []int{1, 3, 2, 5, 4}
	mx := newMonoidSeg(data, func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}, -1_000_000_000)
	sum := newMonoidSeg(data, func(a, b int) int { return a + b }, 0)
	fmt.Println(mx.query(1, 4))
	fmt.Println(sum.query(0, 5))
}
