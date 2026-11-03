package main

import (
	"math/rand"
	"testing"
)

func brute(a []int) int {
	if len(a) <= 1 {
		return 0
	}
	s := 0
	for _, x := range a {
		s += x
	}
	best := 1 << 60
	for k := 1; k < len(a); k++ {
		if v := brute(a[:k]) + brute(a[k:]); v < best {
			best = v
		}
	}
	return best + s
}

func TestMergeStones(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 200; trial++ {
		a := make([]int, r.Intn(6)+1)
		for i := range a {
			a[i] = r.Intn(9) + 1
		}
		if got, want := mergeStones(a), brute(a); got != want {
			t.Fatalf("%v: got %d want %d", a, got, want)
		}
	}
}
