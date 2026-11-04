package main

import (
	"fmt"
	"sort"
)

type DSU struct{ parent, size []int }

func NewDSU(n int) *DSU {
	p, s := make([]int, n), make([]int, n)
	for i := range p {
		p[i] = i
		s[i] = 1
	}
	return &DSU{p, s}
}

func (d *DSU) Find(x int) int {
	for d.parent[x] != x {
		d.parent[x] = d.parent[d.parent[x]]
		x = d.parent[x]
	}
	return x
}

func (d *DSU) Unite(a, b int) bool {
	a, b = d.Find(a), d.Find(b)
	if a == b {
		return false
	}
	if d.size[a] < d.size[b] {
		a, b = b, a
	}
	d.parent[b] = a
	d.size[a] += d.size[b]
	return true
}

// kruskal は辺を重みの小さい順に見て、閉路を作らないものだけ採用する
func kruskal(n int, edges [][3]int, dsu *DSU) int {
	sort.Slice(edges, func(i, j int) bool { return edges[i][2] < edges[j][2] })
	total, used := 0, 0
	for _, e := range edges {
		if dsu.Unite(e[0], e[1]) {
			total += e[2]
			used++
			if used == n-1 {
				break
			}
		}
	}
	return total
}

func main() {
	edges := [][3]int{{0, 1, 1}, {1, 2, 2}, {0, 2, 4}, {2, 3, 1}}
	fmt.Println(kruskal(4, edges, NewDSU(4)))
}
