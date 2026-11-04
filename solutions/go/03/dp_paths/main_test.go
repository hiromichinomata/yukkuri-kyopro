package main

import (
	"math/rand"
	"testing"
)

func TestPaths(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		h, w := r.Intn(4)+1, r.Intn(4)+1
		b := make([][]bool, h)
		for i := range b {
			b[i] = make([]bool, w)
			for j := range b[i] {
				b[i][j] = r.Intn(4) == 0
			}
		}
		var cnt func(i, j int) int
		cnt = func(i, j int) int {
			if i >= h || j >= w || b[i][j] {
				return 0
			}
			if i == h-1 && j == w-1 {
				return 1
			}
			return cnt(i+1, j) + cnt(i, j+1)
		}
		if got, want := paths(h, w, b), cnt(0, 0); got != want {
			t.Fatalf("got %d want %d", got, want)
		}
	}
}
