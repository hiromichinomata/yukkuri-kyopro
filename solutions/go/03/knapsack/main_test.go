package main

import (
	"math/rand"
	"testing"
)

func TestKnapsack(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(7)
		ws, vs := make([]int, n), make([]int, n)
		for i := range ws {
			ws[i], vs[i] = r.Intn(6)+1, r.Intn(9)+1
		}
		cap := r.Intn(16)
		want := 0
		for mask := 0; mask < 1<<n; mask++ {
			w, v := 0, 0
			for i := 0; i < n; i++ {
				if mask>>i&1 == 1 {
					w += ws[i]
					v += vs[i]
				}
			}
			if w <= cap && v > want {
				want = v
			}
		}
		if got := knapsack(ws, vs, cap); got != want {
			t.Fatalf("got %d want %d", got, want)
		}
	}
}
