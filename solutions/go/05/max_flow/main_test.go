package main

import (
	"math/rand"
	"testing"
)

func TestMaxFlow(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(5) + 2
		c := make([][]int, n)
		for i := range c {
			c[i] = make([]int, n)
		}
		orig := make([][]int, n)
		for k := r.Intn(12); k > 0; k-- {
			u, v := r.Intn(n), r.Intn(n)
			if u != v {
				c[u][v] += r.Intn(9) + 1
			}
		}
		for i := range c {
			orig[i] = append([]int(nil), c[i]...)
		}
		want := 1 << 60
		for mask := 0; mask < 1<<n; mask++ {
			if mask&1 == 0 || mask>>(n-1)&1 == 1 {
				continue
			}
			cut := 0
			for u := 0; u < n; u++ {
				for v := 0; v < n; v++ {
					if mask>>u&1 == 1 && mask>>v&1 == 0 {
						cut += orig[u][v]
					}
				}
			}
			if cut < want {
				want = cut
			}
		}
		if got := maxFlow(c, 0, n-1, n); got != want {
			t.Fatalf("got %d want %d", got, want)
		}
	}
}
