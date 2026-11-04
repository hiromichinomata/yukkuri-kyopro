package main

import (
	"math/rand"
	"testing"
)

func isSubseq(sub, t string) bool {
	j := 0
	for i := 0; i < len(t) && j < len(sub); i++ {
		if t[i] == sub[j] {
			j++
		}
	}
	return j == len(sub)
}

func TestLcs(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		mk := func() string {
			b := make([]byte, r.Intn(7))
			for i := range b {
				b[i] = "abc"[r.Intn(3)]
			}
			return string(b)
		}
		s, u := mk(), mk()
		want := 0
		for mask := 0; mask < 1<<len(s); mask++ {
			sub := []byte{}
			for i := range s {
				if mask>>i&1 == 1 {
					sub = append(sub, s[i])
				}
			}
			if isSubseq(string(sub), u) && len(sub) > want {
				want = len(sub)
			}
		}
		if got := lcs(s, u); got != want {
			t.Fatalf("%q %q got %d want %d", s, u, got, want)
		}
	}
}
