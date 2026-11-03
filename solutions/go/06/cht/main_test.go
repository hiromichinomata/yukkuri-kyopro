package main

import (
	"math/rand"
	"sort"
	"testing"
)

func TestCHT(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		set := map[line]bool{}
		for k := r.Intn(6) + 1; k > 0; k-- {
			set[line{r.Intn(13) - 6, r.Intn(21) - 10}] = true
		}
		var lines []line
		for l := range set {
			lines = append(lines, l)
		}
		sort.Slice(lines, func(i, j int) bool {
			if lines[i].m != lines[j].m {
				return lines[i].m > lines[j].m
			}
			return lines[i].b < lines[j].b
		})
		dq := chtMin(lines)
		for x := -6; x <= 6; x++ {
			want := 1 << 60
			for _, l := range lines {
				if v := l.eval(x); v < want {
					want = v
				}
			}
			if got := query(&dq, x); got != want {
				t.Fatalf("lines=%v x=%d got %d want %d", lines, x, got, want)
			}
		}
	}
}
