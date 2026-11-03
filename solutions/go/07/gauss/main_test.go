package main

import (
	"math/rand"
	"testing"
)

func TestGauss(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(4) + 1
		x := make([]int, n)
		for i := range x {
			x[i] = r.Intn(6)
		}
		A := make([][]int, n)
		for i := range A {
			A[i] = make([]int, n+1)
			s := 0
			for j := 0; j < n; j++ {
				A[i][j] = r.Intn(4)
				s += A[i][j] * x[j]
			}
			A[i][n] = s % mod
		}
		res := gauss(A)
		for _, row := range res {
			s := 0
			for j := 0; j < n; j++ {
				s = (s + row[j]*x[j]) % mod
			}
			if s != row[n]%mod {
				t.Fatalf("x=%v does not satisfy reduced row %v", x, row)
			}
		}
		for i, row := range res {
			for j := 0; j < n; j++ {
				if row[j] != 0 {
					if row[j] != 1 {
						t.Fatalf("pivot not 1: %v", res)
					}
					for k := range res {
						if k != i && res[k][j] != 0 {
							t.Fatalf("pivot column not cleared: %v", res)
						}
					}
					break
				}
			}
		}
	}
}
