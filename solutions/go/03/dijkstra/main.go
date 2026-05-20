package main

import (
	"container/heap"
	"fmt"
)

type edge struct{ to, cost int }
type item struct{ d, v int }
type pq []item

func (h pq) Len() int            { return len(h) }
func (h pq) Less(i, j int) bool { return h[i].d < h[j].d }
func (h pq) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *pq) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *pq) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func dijkstra(g [][]edge, start, n int) []int {
	const INF = 1 << 60
	dist := make([]int, n)
	for i := range dist {
		dist[i] = INF
	}
	dist[start] = 0
	h := &pq{{0, start}}
	heap.Init(h)
	for h.Len() > 0 {
		it := heap.Pop(h).(item)
		d, v := it.d, it.v
		if d > dist[v] {
			continue
		}
		for _, e := range g[v] {
			nd := d + e.cost
			if nd < dist[e.to] {
				dist[e.to] = nd
				heap.Push(h, item{nd, e.to})
			}
		}
	}
	return dist
}

func main() {
	n := 4
	g := make([][]edge, n)
	add := func(u, v, c int) {
		g[u] = append(g[u], edge{v, c})
		g[v] = append(g[v], edge{u, c})
	}
	add(0, 1, 1)
	add(0, 2, 4)
	add(1, 2, 2)
	add(1, 3, 6)
	add(2, 3, 1)
	fmt.Println(dijkstra(g, 0, n)[3])
}
