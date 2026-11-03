package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type DSU struct {
	parent, size []int
}

func NewDSU(n int) *DSU {
	d := &DSU{make([]int, n), make([]int, n)}
	for i := range d.parent {
		d.parent[i] = i
		d.size[i] = 1
	}
	return d
}

func (d *DSU) Find(x int) int {
	for d.parent[x] != x {
		d.parent[x] = d.parent[d.parent[x]]
		x = d.parent[x]
	}
	return x
}

func (d *DSU) Unite(a, b int) {
	a, b = d.Find(a), d.Find(b)
	if d.size[a] < d.size[b] {
		a, b = b, a
	}
	d.parent[b] = a
	d.size[a] += d.size[b]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	edges := make([][3]int, n-1) // {w, u, v}
	for i := range edges {
		var u, v, w int
		fmt.Fscan(in, &u, &v, &w)
		edges[i] = [3]int{w, u - 1, v - 1}
	}
	sort.Slice(edges, func(i, j int) bool { return edges[i][0] < edges[j][0] })
	d := NewDSU(n)
	ans := 0
	// 重みの小さい辺から順につなぐ。辺 (u, v, w) をつないだ瞬間に初めて行き来できるようになる
	// 頂点の組は size[u 側] × size[v 側] 組あり、その組の f はちょうど w（主客転倒）
	for _, e := range edges {
		w, u, v := e[0], e[1], e[2]
		ans += w * d.size[d.Find(u)] * d.size[d.Find(v)]
		d.Unite(u, v)
	}
	fmt.Println(ans)
}
