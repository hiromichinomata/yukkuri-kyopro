package main

import (
	"math/rand"
	"testing"
)

// p が他の点の作る線分・三角形に（境界含め）含まれるなら凸包の頂点ではない
func covered(p point, others []point) bool {
	in := func(a, b point) bool {
		return ccw(a, b, p) == 0 && min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x) && min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y)
	}
	for i := range others {
		for j := i + 1; j < len(others); j++ {
			if in(others[i], others[j]) {
				return true
			}
			for k := j + 1; k < len(others); k++ {
				a, b, c := others[i], others[j], others[k]
				if ccw(a, b, c) == 0 {
					continue
				}
				s1, s2, s3 := ccw(a, b, p), ccw(b, c, p), ccw(c, a, p)
				if (s1 >= 0 && s2 >= 0 && s3 >= 0) || (s1 <= 0 && s2 <= 0 && s3 <= 0) {
					return true
				}
			}
		}
	}
	return false
}

func TestConvexHull(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		pts := make([]point, r.Intn(10)+1)
		uniq := map[point]bool{}
		for i := range pts {
			pts[i] = point{r.Intn(6), r.Intn(6)}
			uniq[pts[i]] = true
		}
		want := map[point]bool{}
		for p := range uniq {
			var others []point
			for q := range uniq {
				if q != p {
					others = append(others, q)
				}
			}
			if !covered(p, others) {
				want[p] = true
			}
		}
		got := convexHull(append([]point(nil), pts...))
		gs := map[point]bool{}
		for _, p := range got {
			gs[p] = true
		}
		if len(gs) != len(got) || len(gs) != len(want) {
			t.Fatalf("pts=%v got %v want %v", pts, got, want)
		}
		for p := range want {
			if !gs[p] {
				t.Fatalf("pts=%v got %v want %v", pts, got, want)
			}
		}
	}
}

func TestConvexHullDuplicates(t *testing.T) {
	for _, pts := range [][]point{{{1, 1}, {1, 1}}, {{0, 0}, {0, 0}, {2, 0}}, {{0, 0}, {1, 1}, {1, 1}, {2, 0}}} {
		got := convexHull(append([]point(nil), pts...))
		seen := map[point]bool{}
		for _, p := range got {
			if seen[p] {
				t.Fatalf("pts=%v: duplicate in %v", pts, got)
			}
			seen[p] = true
		}
	}
}
