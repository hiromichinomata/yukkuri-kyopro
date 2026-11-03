package main

import (
	"math/rand"
	"reflect"
	"testing"
)

func randStr(r *rand.Rand, n int) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = "ab"[r.Intn(2)]
	}
	return string(b)
}

func TestKmpSearch(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 500; trial++ {
		text, pat := randStr(r, r.Intn(12)+1), randStr(r, r.Intn(4)+1)
		want := []int{}
		for i := 0; i+len(pat) <= len(text); i++ {
			if text[i:i+len(pat)] == pat {
				want = append(want, i)
			}
		}
		got := kmpSearch(text, pat)
		if len(got) == 0 && len(want) == 0 {
			continue
		}
		if !reflect.DeepEqual(got, want) {
			t.Fatalf("%q %q got %v want %v", text, pat, got, want)
		}
	}
}
