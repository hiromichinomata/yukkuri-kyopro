package main

import (
	"math/rand"
	"reflect"
	"testing"
)

func TestDijkstra(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(7) + 1
		g := make([][]edge, n)
		type e3 struct{ u, v, c int }
		var es []e3
		for k := r.Intn(15); k > 0; k-- {
			x := e3{r.Intn(n), r.Intn(n), r.Intn(10)}
			es = append(es, x)
			g[x.u] = append(g[x.u], edge{x.v, x.c})
		}
		const inf = 1 << 60
		d := make([]int, n)
		for i := range d {
			d[i] = inf
		}
		d[0] = 0
		for k := 0; k < n; k++ {
			for _, x := range es {
				if d[x.u] < inf && d[x.u]+x.c < d[x.v] {
					d[x.v] = d[x.u] + x.c
				}
			}
		}
		if got := dijkstra(g, 0, n); !reflect.DeepEqual(got, d) {
			t.Fatalf("got %v want %v", got, d)
		}
	}
}
