package main

import (
	"math/rand"
	"testing"
)

func TestCountSubarrayLeK(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		xs := make([]int, r.Intn(9))
		for i := range xs {
			xs[i] = r.Intn(7)
		}
		k := r.Intn(13)
		want := 0
		for l := range xs {
			s := 0
			for rr := l; rr < len(xs); rr++ {
				s += xs[rr]
				if s <= k {
					want++
				}
			}
		}
		if got := countSubarrayLeK(xs, k); got != want {
			t.Fatalf("%v k=%d got %d want %d", xs, k, got, want)
		}
	}
}
