package main

import (
	"math/rand"
	"testing"
)

func TestIsBipartite(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(7) + 1
		g := make([][]int, n)
		var es [][2]int
		for k := r.Intn(10); k > 0; k-- {
			u, v := r.Intn(n), r.Intn(n)
			if u == v {
				continue
			}
			es = append(es, [2]int{u, v})
			g[u] = append(g[u], v)
			g[v] = append(g[v], u)
		}
		want := false
		for mask := 0; mask < 1<<n; mask++ {
			ok := true
			for _, e := range es {
				if mask>>e[0]&1 == mask>>e[1]&1 {
					ok = false
				}
			}
			if ok {
				want = true
				break
			}
		}
		if isBipartite(g, n) != want {
			t.Fatalf("n=%d es=%v want %v", n, es, want)
		}
	}
}
