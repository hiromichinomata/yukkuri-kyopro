package main

import (
	"math/rand"
	"testing"
)

func TestPersistentSegTree(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 100; trial++ {
		n := r.Intn(10) + 1
		arr := make([]int, n)
		for i := range arr {
			arr[i] = r.Intn(10)
		}
		roots := []*node{build(0, n-1, arr)}
		vers := [][]int{append([]int(nil), arr...)}
		for k := 0; k < 20; k++ {
			v := r.Intn(len(roots))
			i, d := r.Intn(n), r.Intn(11)-5
			roots = append(roots, update(roots[v], 0, n-1, i, d))
			nv := append([]int(nil), vers[v]...)
			nv[i] += d
			vers = append(vers, nv)
			q := r.Intn(len(roots))
			l := r.Intn(n)
			rr := l + r.Intn(n-l)
			want := 0
			for j := l; j <= rr; j++ {
				want += vers[q][j]
			}
			if got := query(roots[q], 0, n-1, l, rr); got != want {
				t.Fatalf("got %d want %d", got, want)
			}
		}
	}
}
