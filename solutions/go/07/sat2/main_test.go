package main

import (
	"math/rand"
	"testing"
)

func TestSat2(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 500; trial++ {
		nv := r.Intn(4) + 1
		var clauses, imp [][2]int
		for k := r.Intn(6) + 1; k > 0; k-- {
			a, b := r.Intn(2*nv), r.Intn(2*nv)
			clauses = append(clauses, [2]int{a, b})
			// 節 (a ∨ b) → ¬a ⇒ b, ¬b ⇒ a。リテラル 2i = x_i, 2i+1 = ¬x_i
			imp = addClause(imp, a, b)
		}
		val := func(lit, mask int) bool { return (mask>>(lit/2)&1)^(lit&1) == 1 }
		want := false
		for mask := 0; mask < 1<<nv; mask++ {
			ok := true
			for _, c := range clauses {
				if !val(c[0], mask) && !val(c[1], mask) {
					ok = false
				}
			}
			if ok {
				want = true
			}
		}
		if got := sat2Solvable(imp, nv); got != want {
			t.Fatalf("clauses=%v got %v want %v", clauses, got, want)
		}
	}
}
