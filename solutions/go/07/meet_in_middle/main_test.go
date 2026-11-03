package main

import (
	"math/rand"
	"testing"
)

func TestCanMakeSum(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 500; trial++ {
		xs := make([]int, r.Intn(9))
		for i := range xs {
			xs[i] = r.Intn(15) + 1
		}
		target := r.Intn(41)
		want := false
		for mask := 0; mask < 1<<len(xs); mask++ {
			s := 0
			for i := range xs {
				if mask>>i&1 == 1 {
					s += xs[i]
				}
			}
			if s == target {
				want = true
			}
		}
		if got := canMakeSum(xs, target); got != want {
			t.Fatalf("%v %d got %v want %v", xs, target, got, want)
		}
	}
}
