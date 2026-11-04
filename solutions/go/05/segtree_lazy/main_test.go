package main

import (
	"math/rand"
	"testing"
)

func TestLazySeg(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 100; trial++ {
		n := r.Intn(16) + 1
		a := make([]int, n)
		for i := range a {
			a[i] = r.Intn(11) - 5
		}
		st := NewLazySeg(a)
		for k := 0; k < 60; k++ {
			l := r.Intn(n)
			rr := l + r.Intn(n-l) + 1
			if r.Intn(2) == 0 {
				x := r.Intn(11) - 5
				st.RangeAdd(l, rr, int64(x))
				for i := l; i < rr; i++ {
					a[i] += x
				}
			} else {
				want := 0
				for i := l; i < rr; i++ {
					want += a[i]
				}
				if got := st.RangeSum(l, rr); got != int64(want) {
					t.Fatalf("got %d want %d", got, want)
				}
			}
		}
	}
}
