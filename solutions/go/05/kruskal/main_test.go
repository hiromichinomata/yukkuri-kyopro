package main

import (
	"math/rand"
	"testing"
)

// mst は解答の kruskal（辺を重み順に見て DSU で閉路を避ける）
func mst(n int, es [][3]int) int {
	return kruskal(n, append([][3]int(nil), es...), NewDSU(n))
}

func TestKruskalDSU(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 200; trial++ {
		n := r.Intn(5) + 1
		var es [][3]int
		for k := r.Intn(8); k > 0; k-- {
			u, v := r.Intn(n), r.Intn(n)
			if u != v {
				es = append(es, [3]int{u, v, r.Intn(9) + 1})
			}
		}
		comps := func(sub [][3]int) (int, bool) {
			d := NewDSU(n)
			forest := true
			for _, e := range sub {
				if !d.Unite(e[0], e[1]) {
					forest = false
				}
			}
			c := 0
			for i := 0; i < n; i++ {
				if d.Find(i) == i {
					c++
				}
			}
			return c, forest
		}
		full, _ := comps(es)
		want := 1 << 60
		for mask := 0; mask < 1<<len(es); mask++ {
			var sub [][3]int
			w := 0
			for i, e := range es {
				if mask>>i&1 == 1 {
					sub = append(sub, e)
					w += e[2]
				}
			}
			if c, ok := comps(sub); ok && c == full && w < want {
				want = w
			}
		}
		if got := mst(n, es); got != want {
			t.Fatalf("got %d want %d", got, want)
		}
	}
}
