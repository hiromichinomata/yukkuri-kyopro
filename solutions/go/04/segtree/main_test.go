package main

import (
	"math/rand"
	"testing"
)

func TestSegTree(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 50; trial++ {
		n := r.Intn(20) + 1
		a := make([]int, n)
		for i := range a {
			a[i] = r.Intn(11) - 5
		}
		s := NewSegTree(a)
		for k := 0; k < 50; k++ {
			i, x := r.Intn(n), r.Intn(11)-5
			s.Update(i, x)
			a[i] = x
			l := r.Intn(n)
			rr := l + r.Intn(n-l) + 1
			want := 0
			for j := l; j < rr; j++ {
				want += a[j]
			}
			if got := s.Query(l, rr); got != want {
				t.Fatalf("got %d want %d", got, want)
			}
		}
	}
}
