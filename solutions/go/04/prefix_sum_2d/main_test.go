package main

import (
	"math/rand"
	"testing"
)

func TestRectSum(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		h, w := r.Intn(5)+1, r.Intn(5)+1
		a := make([][]int, h)
		for i := range a {
			a[i] = make([]int, w)
			for j := range a[i] {
				a[i][j] = r.Intn(19) - 9
			}
		}
		s := build2D(a)
		h1 := r.Intn(h) + 1
		h2 := h1 + r.Intn(h-h1+1)
		w1 := r.Intn(w) + 1
		w2 := w1 + r.Intn(w-w1+1)
		want := 0
		for i := h1 - 1; i < h2; i++ {
			for j := w1 - 1; j < w2; j++ {
				want += a[i][j]
			}
		}
		if got := rectSum(s, h1, w1, h2, w2); got != want {
			t.Fatalf("got %d want %d", got, want)
		}
	}
}
