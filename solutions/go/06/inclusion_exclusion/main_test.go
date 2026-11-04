package main

import "testing"

func TestCountCoprime(t *testing.T) {
	for n := 0; n < 200; n++ {
		want := 0
		for i := 1; i <= n; i++ {
			if i%2 != 0 && i%3 != 0 {
				want++
			}
		}
		if got := countCoprime(n); got != want {
			t.Fatalf("n=%d got %d want %d", n, got, want)
		}
	}
}
