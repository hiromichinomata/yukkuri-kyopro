package main

import (
	"fmt"
)

type edge struct {
	to, cap, rev int
}

type Dinic struct {
	n   int
	g   [][]edge
}

func NewDinic(n int) *Dinic {
	g := make([][]edge, n)
	return &Dinic{n, g}
}

func (d *Dinic) AddEdge(fr, to, cap int) {
	d.g[fr] = append(d.g[fr], edge{to, cap, len(d.g[to])})
	d.g[to] = append(d.g[to], edge{fr, 0, len(d.g[fr]) - 1})
}

func (d *Dinic) bfs(s, t int, level []int) bool {
	for i := range level {
		level[i] = -1
	}
	level[s] = 0
	q := []int{s}
	for head := 0; head < len(q); head++ {
		v := q[head]
		for _, e := range d.g[v] {
			if e.cap > 0 && level[e.to] < 0 {
				level[e.to] = level[v] + 1
				q = append(q, e.to)
			}
		}
	}
	return level[t] >= 0
}

func (d *Dinic) dfs(v, t, f int, level, iter []int) int {
	if v == t {
		return f
	}
	for i := iter[v]; i < len(d.g[v]); i++ {
		iter[v] = i
		e := d.g[v][i]
		if e.cap > 0 && level[v] < level[e.to] {
			df := d.dfs(e.to, t, min(f, e.cap), level, iter)
			if df > 0 {
				d.g[v][i].cap -= df
				d.g[e.to][e.rev].cap += df
				return df
			}
		}
	}
	return 0
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func (d *Dinic) MaxFlow(s, t int) int {
	flow := 0
	level := make([]int, d.n)
	for d.bfs(s, t, level) {
		iter := make([]int, d.n)
		for {
			f := d.dfs(s, t, 1<<30, level, iter)
			if f == 0 {
				break
			}
			flow += f
		}
	}
	return flow
}

func main() {
	d := NewDinic(4)
	d.AddEdge(0, 1, 3)
	d.AddEdge(0, 2, 2)
	d.AddEdge(1, 2, 1)
	d.AddEdge(1, 3, 2)
	d.AddEdge(2, 3, 3)
	fmt.Println(d.MaxFlow(0, 3))
}
