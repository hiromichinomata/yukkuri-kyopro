package main

import (
	"math/rand"
	"reflect"
	"testing"
)

func TestMoCountDistinct(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		n := r.Intn(15) + 1
		a := make([]int, n)
		for i := range a {
			a[i] = r.Intn(5)
		}
		qs := make([][2]int, r.Intn(8)+1)
		want := make([]int, len(qs))
		for i := range qs {
			l := r.Intn(n)
			rr := l + r.Intn(n-l)
			qs[i] = [2]int{l, rr}
			seen := map[int]bool{}
			for _, x := range a[l : rr+1] {
				seen[x] = true
			}
			want[i] = len(seen)
		}
		if got := moCountDistinct(a, qs); !reflect.DeepEqual(got, want) {
			t.Fatalf("a=%v qs=%v got %v want %v", a, qs, got, want)
		}
	}
}
