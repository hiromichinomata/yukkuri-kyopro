package main

import (
	"math/rand"
	"testing"
)

func TestZAlgorithm(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 500; trial++ {
		b := make([]byte, r.Intn(12)+1)
		for i := range b {
			b[i] = "ab"[r.Intn(2)]
		}
		s := string(b)
		z := zAlgorithm(s)
		for i := 1; i < len(s); i++ {
			k := 0
			for i+k < len(s) && s[k] == s[i+k] {
				k++
			}
			if z[i] != k {
				t.Fatalf("%q i=%d got %d want %d", s, i, z[i], k)
			}
		}
	}
}
