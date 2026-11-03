package main

import (
	"math/rand"
	"testing"
)

func TestMaxSumK(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		xs := make([]int, r.Intn(10)+1)
		for i := range xs {
			xs[i] = r.Intn(19) - 9
		}
		k := r.Intn(len(xs)) + 1
		want := -1 << 60
		for i := 0; i+k <= len(xs); i++ {
			s := 0
			for _, x := range xs[i : i+k] {
				s += x
			}
			if s > want {
				want = s
			}
		}
		if got := maxSumK(xs, k); got != want {
			t.Fatalf("%v k=%d got %d want %d", xs, k, got, want)
		}
	}
}
