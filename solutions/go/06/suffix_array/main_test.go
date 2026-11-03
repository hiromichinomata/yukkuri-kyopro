package main

import (
	"math/rand"
	"reflect"
	"sort"
	"testing"
)

func TestSuffixArray(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 500; trial++ {
		b := make([]byte, r.Intn(12)+1)
		for i := range b {
			b[i] = "ab"[r.Intn(2)]
		}
		s := string(b)
		want := make([]int, len(s))
		for i := range want {
			want[i] = i
		}
		sort.Slice(want, func(i, j int) bool { return s[want[i]:] < s[want[j]:] })
		if got := suffixArray(s); !reflect.DeepEqual(got, want) {
			t.Fatalf("%q got %v want %v", s, got, want)
		}
	}
}
