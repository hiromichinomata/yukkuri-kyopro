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

func (d *DSU) Same(a, b int) bool {
	return d.Find(a) == d.Find(b)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, q int
	fmt.Fscan(in, &n, &q)
	d := NewDSU(n)
	for ; q > 0; q-- {
		var t, u, v int
		fmt.Fscan(in, &t, &u, &v)
		u--
		v--
		if t == 1 {
			d.Unite(u, v)
		} else {
			if d.Same(u, v) {
				fmt.Fprintln(out, "Yes")
			} else {
				fmt.Fprintln(out, "No")
			}
		}
	}
}
