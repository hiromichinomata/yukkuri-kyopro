package main

import "testing"

func TestNcr(t *testing.T) {
	fac, inv := prepareFac(60)
	// パスカルの三角形と比べる
	c := make([][]int, 61)
	for n := 0; n <= 60; n++ {
		c[n] = make([]int, n+1)
		c[n][0], c[n][n] = 1, 1
		for r := 1; r < n; r++ {
			c[n][r] = (c[n-1][r-1] + c[n-1][r]) % mod
		}
		for r := -1; r <= n+1; r++ {
			want := 0
			if 0 <= r && r <= n {
				want = c[n][r]
			}
			if got := ncr(n, r, fac, inv); got != want {
				t.Fatalf("C(%d,%d) got %d want %d", n, r, got, want)
			}
		}
	}
}
