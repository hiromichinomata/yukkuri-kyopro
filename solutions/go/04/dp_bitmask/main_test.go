package main

import (
	"math/rand"
	"testing"
)

func perms(a []int, k int, f func([]int)) {
	if k == len(a) {
		f(a)
		return
	}
	for i := k; i < len(a); i++ {
		a[k], a[i] = a[i], a[k]
		perms(a, k+1, f)
		a[k], a[i] = a[i], a[k]
	}
}

func TestTsp(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 100; trial++ {
		n := r.Intn(6) + 1
		d := make([][]int, n)
		for i := range d {
			d[i] = make([]int, n)
			for j := range d[i] {
				if i != j {
					d[i][j] = r.Intn(20) + 1
				}
			}
		}
		rest := make([]int, n-1)
		for i := range rest {
			rest[i] = i + 1
		}
		want := 1 << 60
		perms(rest, 0, func(p []int) {
			cur, c := 0, 0
			for _, v := range p {
				c += d[cur][v]
				cur = v
			}
			if c < want {
				want = c
			}
		})
		if got := tsp(d, n); got != want {
			t.Fatalf("got %d want %d", got, want)
		}
	}
}
