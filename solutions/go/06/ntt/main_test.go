package main

import (
	"math/rand"
	"reflect"
	"testing"
)

func TestConvolution(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		a := make([]int, r.Intn(9)+1)
		b := make([]int, r.Intn(9)+1)
		for i := range a {
			a[i] = r.Intn(51)
		}
		for i := range b {
			b[i] = r.Intn(51)
		}
		want := make([]int, len(a)+len(b)-1)
		for i := range a {
			for j := range b {
				want[i+j] += a[i] * b[j]
			}
		}
		if got := convolution(a, b); !reflect.DeepEqual(got, want) {
			t.Fatalf("%v * %v got %v want %v", a, b, got, want)
		}
	}
}
