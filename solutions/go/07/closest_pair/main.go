package main

import (
	"fmt"
	"math"
	"sort"
)

type point struct{ x, y int }

func dist2(a, b point) int {
	dx := a.x - b.x
	dy := a.y - b.y
	return dx*dx + dy*dy
}

func closestPair(points []point) int {
	sort.Slice(points, func(i, j int) bool { return points[i].x < points[j].x })
	n := len(points)
	if n <= 1 {
		return 0
	}
	var solve func(l, r int) int
	solve = func(l, r int) int {
		if r-l <= 3 {
			best := int(1e18)
			for i := l; i < r; i++ {
				for j := i + 1; j < r; j++ {
					best = min(best, dist2(points[i], points[j]))
				}
			}
			return best
		}
		mid := (l + r) / 2
		midx := points[mid].x
		d := min(solve(l, mid), solve(mid, r))
		var strip []point
		for _, p := range points[l:r] {
			dx := p.x - midx
			if dx*dx < d {
				strip = append(strip, p)
			}
		}
		sort.Slice(strip, func(i, j int) bool { return strip[i].y < strip[j].y })
		for i := 0; i < len(strip); i++ {
			for j := i + 1; j < len(strip) && j < i+8; j++ {
				d = min(d, dist2(strip[i], strip[j]))
			}
		}
		return d
	}
	return solve(0, n)
}

func main() {
	pts := []point{{0, 0}, {1, 1}, {3, 4}, {0, 5}, {2, 2}}
	fmt.Println(math.Sqrt(float64(closestPair(pts))))
}
