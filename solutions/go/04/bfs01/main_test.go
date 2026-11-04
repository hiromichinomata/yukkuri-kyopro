package main

import (
	"math/rand"
	"reflect"
	"testing"
)

func TestBfs01(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(7) + 1
		type e struct{ u, v, c int }
		var es []e
		g := make([][]struct{ to, cost int }, n)
		for k := r.Intn(15); k > 0; k-- {
			x := e{r.Intn(n), r.Intn(n), r.Intn(2)}
			es = append(es, x)
			g[x.u] = append(g[x.u], struct{ to, cost int }{x.v, x.c})
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
		got := bfs01(g, 0, n)
		for i := range got {
			if got[i] >= inf {
				got[i] = inf
			}
		}
		if !reflect.DeepEqual(got, d) {
			t.Fatalf("got %v want %v", got, d)
		}
	}
}
