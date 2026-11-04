package main

import (
	"math/rand"
	"testing"
)

func TestSCC(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(7) + 1
		g := make([][]int, n)
		reach := make([][]bool, n)
		for i := range reach {
			reach[i] = make([]bool, n)
			reach[i][i] = true
		}
		var es [][2]int
		for k := r.Intn(12); k > 0; k-- {
			u, v := r.Intn(n), r.Intn(n)
			if u != v {
				g[u] = append(g[u], v)
				reach[u][v] = true
				es = append(es, [2]int{u, v})
			}
		}
		for k := 0; k < n; k++ {
			for i := 0; i < n; i++ {
				for j := 0; j < n; j++ {
					reach[i][j] = reach[i][j] || (reach[i][k] && reach[k][j])
				}
			}
		}
		comp, _ := scc(g, n)
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if (comp[i] == comp[j]) != (reach[i][j] && reach[j][i]) {
					t.Fatalf("comp=%v es=%v", comp, es)
				}
			}
		}
		for _, e := range es {
			if comp[e[0]] > comp[e[1]] {
				t.Fatalf("not topological: comp=%v es=%v", comp, es)
			}
		}
	}
}
