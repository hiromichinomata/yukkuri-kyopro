package main

import (
	"math/rand"
	"testing"
)

func TestClosestPair(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 500; trial++ {
		pts := make([]point, r.Intn(19)+2)
		for i := range pts {
			pts[i] = point{r.Intn(31), r.Intn(31)}
		}
		want := 1 << 60
		for i := range pts {
			for j := i + 1; j < len(pts); j++ {
				if d := dist2(pts[i], pts[j]); d < want {
					want = d
				}
			}
		}
		if got := closestPair(append([]point(nil), pts...)); got != want {
			t.Fatalf("%v got %d want %d", pts, got, want)
		}
	}
}
