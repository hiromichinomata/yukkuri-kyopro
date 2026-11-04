package main

import (
	"fmt"
	"strings"
)

func bfs01(g [][]struct{ to, cost int }, start, n int) []int {
	const INF = 1 << 60
	dist := make([]int, n)
	for i := range dist {
		dist[i] = INF
	}
	dist[start] = 0
	// deque を 2 本のスライスで表す: front は末尾が先頭（コスト 0 を積む）、back は普通のキュー（コスト 1）
	front := []int{start}
	back := []int{}
	for len(front) > 0 || len(back) > 0 {
		var v int
		if len(front) > 0 {
			v = front[len(front)-1]
			front = front[:len(front)-1]
		} else {
			v = back[0]
			back = back[1:]
		}
		for _, e := range g[v] {
			nd := dist[v] + e.cost
			if nd < dist[e.to] {
				dist[e.to] = nd
				if e.cost == 0 {
					front = append(front, e.to)
				} else {
					back = append(back, e.to)
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
	fmt.Println(strings.Trim(fmt.Sprint(bfs01(g, 0, n)), "[]"))
}
