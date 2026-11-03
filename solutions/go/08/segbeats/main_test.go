package main

import (
	"math/rand"
	"testing"
)

func TestSegBeats(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(10) + 1
		a := make([]int, n)
		for i := range a {
			a[i] = r.Intn(21)
		}
		st := newSegBeats(a)
		for k := 0; k < 30; k++ {
			l := r.Intn(n)
			rr := l + r.Intn(n-l)
			if r.Intn(2) == 0 {
				x := r.Intn(21)
				st.RangeChmin(l, rr, x)
				for i := l; i <= rr; i++ {
					if a[i] > x {
						a[i] = x
					}
				}
			} else {
				want := 0
				for i := l; i <= rr; i++ {
					want += a[i]
				}
				if got := st.RangeSum(l, rr); got != want {
					t.Fatalf("got %d want %d", got, want)
				}
			}
		}
	}
}
