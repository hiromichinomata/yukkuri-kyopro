package main

import "fmt"

func isBipartite(g [][]int, n int) bool {
	color := make([]int, n)
	for i := range color {
		color[i] = -1
	}
	for s := 0; s < n; s++ {
		if color[s] != -1 {
			continue
		}
		color[s] = 0
		q := []int{s}
		for head := 0; head < len(q); head++ {
			v := q[head]
			for _, to := range g[v] {
				if color[to] == -1 {
					color[to] = color[v] ^ 1
					q = append(q, to)
				} else if color[to] == color[v] {
					return false
				}
			}
		}
	}
	return true
}

func main() {
	g := [][]int{{1, 3}, {0, 2}, {1, 3}, {0, 2}}
	fmt.Println(isBipartite(g, 4))
	g2 := [][]int{{1, 2}, {0, 2}, {0, 1}}
	fmt.Println(isBipartite(g2, 3))
}
