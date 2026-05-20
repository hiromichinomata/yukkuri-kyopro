package main

import "fmt"

type XorBasis struct {
	b []int
}

func NewXorBasis(bits int) *XorBasis {
	return &XorBasis{b: make([]int, bits)}
}

func (x *XorBasis) Add(v int) bool {
	for i := len(x.b) - 1; i >= 0; i-- {
		if (v>>i)&1 == 0 {
			continue
		}
		if x.b[i] == 0 {
			x.b[i] = v
			return true
		}
		v ^= x.b[i]
	}
	return false
}

func (x *XorBasis) MaxXor() int {
	res := 0
	for i := len(x.b) - 1; i >= 0; i-- {
		if x.b[i] != 0 && (res>>i)&1 == 0 {
			res ^= x.b[i]
		}
	}
	return res
}

func main() {
	basis := NewXorBasis(60)
	for _, v := range []int{8, 4, 2, 1, 5, 3} {
		basis.Add(v)
	}
	fmt.Println(basis.MaxXor())
}
