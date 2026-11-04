package main

import (
	"math/rand"
	"testing"
)

func TestLisLength(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		a := make([]int, r.Intn(9))
		for i := range a {
			a[i] = r.Intn(6)
		}
		want := 0
		for mask := 0; mask < 1<<len(a); mask++ {
			prev, cnt, ok := -1, 0, true
			for i := range a {
				if mask>>i&1 == 1 {
					if a[i] <= prev {
						ok = false
					}
					prev = a[i]
					cnt++
				}
			}
			if ok && cnt > want {
				want = cnt
			}
		}
		if got := lisLength(a); got != want {
			t.Fatalf("%v got %d want %d", a, got, want)
		}
	}
}
