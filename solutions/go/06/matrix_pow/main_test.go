package main

import "testing"

func TestFib(t *testing.T) {
	a, b := 0, 1
	for n := 0; n < 90; n++ {
		if got := fib(n); got != a%1_000_000_007 {
			t.Fatalf("n=%d got %d want %d", n, got, a%1_000_000_007)
		}
		a, b = b, (a+b)%1_000_000_007
	}
}
