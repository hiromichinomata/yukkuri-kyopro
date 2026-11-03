package main

import (
	"math/rand"
	"sort"
	"testing"
)

func TestLowerBound(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 500; trial++ {
		a := make([]int, r.Intn(10))
		for i := range a {
			a[i] = r.Intn(10)
		}
		sort.Ints(a)
		x := r.Intn(12) - 1
		want := 0
		for want < len(a) && a[want] < x {
			want++
		}
		if got := lowerBound(a, x); got != want {
			t.Fatalf("%v x=%d got %d want %d", a, x, got, want)
		}
	}
}
