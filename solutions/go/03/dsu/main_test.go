package main

import (
	"math/rand"
	"testing"
)

func TestDSU(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(8) + 1
		d := NewDSU(n)
		reach := make([][]bool, n)
		for i := range reach {
			reach[i] = make([]bool, n)
			reach[i][i] = true
		}
		for k := r.Intn(9); k > 0; k-- {
			u, v := r.Intn(n), r.Intn(n)
			d.Unite(u, v)
			reach[u][v], reach[v][u] = true, true
		}
		for k := 0; k < n; k++ {
			for i := 0; i < n; i++ {
				for j := 0; j < n; j++ {
					reach[i][j] = reach[i][j] || (reach[i][k] && reach[k][j])
				}
			}
		}
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if d.Same(i, j) != reach[i][j] {
					t.Fatalf("Same(%d,%d) wrong", i, j)
				}
			}
		}
	}
}
