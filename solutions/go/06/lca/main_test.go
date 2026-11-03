package main

import (
	"math/rand"
	"testing"
)

// 根からのパスを親配列でたどる愚直な LCA と比べる（深さ 16 を超える細長い木も含める）
func TestLCA(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(40) + 1
		par := make([]int, n)
		g := make([][]int, n)
		par[0] = -1
		for v := 1; v < n; v++ {
			if r.Intn(3) == 0 {
				par[v] = r.Intn(v)
			} else {
				par[v] = v - 1 // 細長くする
			}
			g[v] = append(g[v], par[v])
			g[par[v]] = append(g[par[v]], v)
		}
		depth, up, LOG := buildLCA(g, 0)
		for k := 0; k < 30; k++ {
			a, b := r.Intn(n), r.Intn(n)
			anc := map[int]bool{}
			for x := a; x != -1; x = par[x] {
				anc[x] = true
			}
			want := b
			for !anc[want] {
				want = par[want]
			}
			if got := lca(a, b, depth, up, LOG); got != want {
				t.Fatalf("lca(%d,%d) got %d want %d", a, b, got, want)
			}
		}
	}
}
