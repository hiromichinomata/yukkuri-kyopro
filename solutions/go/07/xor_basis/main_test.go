package main

import (
	"math/rand"
	"testing"
)

func TestXorBasis(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 500; trial++ {
		xs := make([]int, r.Intn(7))
		b := NewXorBasis(8)
		for i := range xs {
			xs[i] = r.Intn(64)
			b.Add(xs[i])
		}
		want := 0
		for mask := 0; mask < 1<<len(xs); mask++ {
			v := 0
			for i := range xs {
				if mask>>i&1 == 1 {
					v ^= xs[i]
				}
			}
			if v > want {
				want = v
			}
		}
		if got := b.MaxXor(); got != want {
			t.Fatalf("%v got %d want %d", xs, got, want)
		}
	}
}
