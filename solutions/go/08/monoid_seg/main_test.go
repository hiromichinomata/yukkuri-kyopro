package main

import (
	"math/rand"
	"testing"
)

func TestMonoidSeg(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	mx := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}
	// 「左側を優先する」演算は結合的だが非可換。左右の順番を取り違えると落ちる
	const none = 1 << 60
	first := func(a, b int) int {
		if a != none {
			return a
		}
		return b
	}
	for trial := 0; trial < 100; trial++ {
		n := r.Intn(12) + 1
		a := make([]int, n)
		for i := range a {
			a[i] = r.Intn(19) - 9
		}
		s := newMonoidSeg(a, mx, -1<<60)
		for k := 0; k < 40; k++ {
			i, x := r.Intn(n), r.Intn(19)-9
			a[i] = x
			s.update(i, x)
			l := r.Intn(n)
			rr := l + r.Intn(n-l) + 1
			want := -1 << 60
			for j := l; j < rr; j++ {
				want = mx(want, a[j])
			}
			if got := s.query(l, rr); got != want {
				t.Fatalf("max got %d want %d", got, want)
			}
		}
		f := newMonoidSeg(a, first, none)
		for l := 0; l < n; l++ {
			for rr := l + 1; rr <= n; rr++ {
				if got := f.query(l, rr); got != a[l] {
					t.Fatalf("first(%d,%d) got %d want %d", l, rr, got, a[l])
				}
			}
		}
	}
}
