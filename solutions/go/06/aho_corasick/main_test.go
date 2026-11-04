package main

import (
	"math/rand"
	"sort"
	"testing"
)

func TestAhoCorasick(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	rs := func(n int) string {
		b := make([]byte, n)
		for i := range b {
			b[i] = "ab"[r.Intn(2)]
		}
		return string(b)
	}
	for trial := 0; trial < 300; trial++ {
		set := map[string]bool{}
		for k := r.Intn(4) + 1; k > 0; k-- {
			set[rs(r.Intn(3)+1)] = true
		}
		text := rs(r.Intn(13))
		ac := newAhoCorasick()
		var want []hit
		for w := range set {
			ac.add(w)
			for i := 0; i+len(w) <= len(text); i++ {
				if text[i:i+len(w)] == w {
					want = append(want, hit{i + len(w) - 1, w})
				}
			}
		}
		ac.build()
		got := ac.search(text)
		less := func(h []hit) func(i, j int) bool {
			return func(i, j int) bool {
				if h[i].end != h[j].end {
					return h[i].end < h[j].end
				}
				return h[i].word < h[j].word
			}
		}
		sort.Slice(got, less(got))
		sort.Slice(want, less(want))
		if len(got) != len(want) {
			t.Fatalf("text=%q got %v want %v", text, got, want)
		}
		for i := range got {
			if got[i] != want[i] {
				t.Fatalf("text=%q got %v want %v", text, got, want)
			}
		}
	}
}
