package main

import (
	"math/big"
	"testing"
)

func TestBuildNCR(t *testing.T) {
	c := buildNCR(60)
	for n := 0; n <= 60; n++ {
		for r := 0; r <= n; r++ {
			want := new(big.Int).Mod(new(big.Int).Binomial(int64(n), int64(r)), big.NewInt(mod)).Int64()
			if int64(c[n][r]) != want {
				t.Fatalf("C(%d,%d) got %d want %d", n, r, c[n][r], want)
			}
		}
	}
}
