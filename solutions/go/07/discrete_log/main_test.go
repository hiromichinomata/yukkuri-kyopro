package main

import "testing"

func TestBsgs(t *testing.T) {
	for _, p := range []int{5, 7, 11, 13, 101} {
		for a := 1; a < p; a++ {
			for b := 1; b < p; b++ {
				want, cur := -1, 1
				for x := 0; x < p-1; x++ {
					if cur == b {
						want = x
						break
					}
					cur = cur * a % p
				}
				if got := bsgs(a, b, p, p-1); got != want {
					t.Fatalf("a=%d b=%d p=%d got %d want %d", a, b, p, got, want)
				}
			}
		}
	}
}
