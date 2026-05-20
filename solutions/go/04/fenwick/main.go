package main

import "fmt"

type Fenwick struct {
	n   int
	bit []int
}

func NewFenwick(n int) *Fenwick {
	return &Fenwick{n, make([]int, n+1)}
}

func (f *Fenwick) Add(i, x int) {
	for i <= f.n {
		f.bit[i] += x
		i += i & -i
	}
}

func (f *Fenwick) Sum(i int) int {
	s := 0
	for i > 0 {
		s += f.bit[i]
		i -= i & -i
	}
	return s
}

func (f *Fenwick) RangeSum(l, r int) int {
	return f.Sum(r) - f.Sum(l-1)
}

func main() {
	fw := NewFenwick(5)
	for i, v := range []int{1, 2, 3, 4, 5} {
		fw.Add(i+1, v)
	}
	fmt.Println(fw.RangeSum(2, 4))
}
