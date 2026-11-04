package main

import (
	"bufio"
	"fmt"
	"os"
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
	if a == b {
		return
	}
	if d.size[a] < d.size[b] {
		a, b = b, a
	}
	d.parent[b] = a
	d.size[a] += d.size[b]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n, &m)
	d := NewDSU(n)
	for i := 0; i < m; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		d.Unite(a-1, b-1)
	}
	// 一番大きい友達グループの人数が答え
	ans := 0
	for v := 0; v < n; v++ {
		if s := d.size[d.Find(v)]; s > ans {
			ans = s
		}
	}
	fmt.Fprintln(out, ans)
}
