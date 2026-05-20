package main

import (
	"fmt"
	"sort"
)

type point struct{ x, y int }

func ccw(a, b, c point) int {
	return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)
}

func convexHull(pts []point) []point {
	sort.Slice(pts, func(i, j int) bool {
		if pts[i].x != pts[j].x {
			return pts[i].x < pts[j].x
		}
		return pts[i].y < pts[j].y
	})
	if len(pts) <= 1 {
		return pts
	}
	lower := []point{}
	for _, p := range pts {
		for len(lower) >= 2 && ccw(lower[len(lower)-2], lower[len(lower)-1], p) <= 0 {
			lower = lower[:len(lower)-1]
		}
		lower = append(lower, p)
	}
	upper := []point{}
	for i := len(pts) - 1; i >= 0; i-- {
		p := pts[i]
		for len(upper) >= 2 && ccw(upper[len(upper)-2], upper[len(upper)-1], p) <= 0 {
			upper = upper[:len(upper)-1]
		}
		upper = append(upper, p)
	}
	return append(lower[:len(lower)-1], upper[:len(upper)-1]...)
}

func main() {
	pts := []point{{0, 0}, {1, 0}, {0, 1}, {1, 1}}
	fmt.Println(convexHull(pts))
}
