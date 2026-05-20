package main

import "fmt"

func main() {
	n := 7
	g := make([][]int, n)
	add := func(u, v int) {
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	add(0, 1)
	add(0, 2)
	add(1, 3)
	add(1, 4)
	add(2, 5)
	add(2, 6)

	parent := make([]int, n)
	depth := make([]int, n)
	size := make([]int, n)
	head := make([]int, n)
	pos := make([]int, n)
	cur := 0

	var dfsSize func(v, p int)
	dfsSize = func(v, p int) {
		size[v] = 1
		parent[v] = p
		for _, to := range g[v] {
			if to == p {
				continue
			}
			depth[to] = depth[v] + 1
			dfsSize(to, v)
			size[v] += size[to]
		}
	}

	var dfsHLD func(v, p, h int)
	dfsHLD = func(v, p, h int) {
		head[v] = h
		pos[v] = cur
		cur++
		heavy := -1
		for _, to := range g[v] {
			if to == p {
				continue
			}
			if heavy == -1 || size[to] > size[heavy] {
				heavy = to
			}
		}
		if heavy != -1 {
			dfsHLD(heavy, v, h)
		}
		for _, to := range g[v] {
			if to != p && to != heavy {
				dfsHLD(to, v, to)
			}
		}
	}

	dfsSize(0, -1)
	dfsHLD(0, -1, 0)

	lca := func(a, b int) int {
		for head[a] != head[b] {
			if depth[head[a]] > depth[head[b]] {
				a = parent[head[a]]
			} else {
				b = parent[head[b]]
			}
		}
		if depth[a] < depth[b] {
			return a
		}
		return b
	}

	fmt.Println(lca(3, 5), lca(4, 6))
	fmt.Println(head, pos)
}
