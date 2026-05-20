package main

import "fmt"

func bfs01(g [][]struct{ to, cost int }, start, n int) []int {
	const INF = 1 << 60
	dist := make([]int, n)
	for i := range dist {
		dist[i] = INF
	}
	dist[start] = 0
	dq := []int{start}
	for head := 0; head < len(dq); head++ {
		v := dq[head]
		for _, e := range g[v] {
			nd := dist[v] + e.cost
			if nd < dist[e.to] {
				dist[e.to] = nd
				if e.cost == 0 {
					dq = append([]int{e.to}, dq...)
				} else {
					dq = append(dq, e.to)
				}
			}
		}
	}
	return dist
}

func main() {
	n := 4
	g := make([][]struct{ to, cost int }, n)
	add := func(u, v, c int) {
		g[u] = append(g[u], struct{ to, cost int }{v, c})
	}
	add(0, 1, 0)
	add(1, 0, 0)
	add(1, 2, 1)
	add(2, 1, 1)
	add(2, 3, 0)
	add(3, 2, 0)
	fmt.Println(bfs01(g, 0, n))
}
