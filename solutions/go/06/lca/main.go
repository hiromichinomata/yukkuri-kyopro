package main

import "fmt"

func main() {
	n := 7
	g := make([][]int, n)
	edges := [][2]int{{0, 1}, {0, 2}, {1, 3}, {1, 4}, {2, 5}, {2, 6}}
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	const LOG = 4
	up := make([][]int, n)
	depth := make([]int, n)
	for i := range up {
		up[i] = make([]int, LOG)
		for j := range up[i] {
			up[i][j] = -1
		}
	}
	var dfs func(v, p int)
	dfs = func(v, p int) {
		up[v][0] = p
		for i := 1; i < LOG; i++ {
			if up[v][i-1] != -1 {
				up[v][i] = up[up[v][i-1]][i-1]
			}
		}
		for _, to := range g[v] {
			if to == p {
				continue
			}
			depth[to] = depth[v] + 1
			dfs(to, v)
		}
	}
	dfs(0, -1)
	lca := func(a, b int) int {
		if depth[a] < depth[b] {
			a, b = b, a
		}
		d := depth[a] - depth[b]
		for i := 0; i < LOG; i++ {
			if d>>i&1 == 1 {
				a = up[a][i]
			}
		}
		if a == b {
			return a
		}
		for i := LOG - 1; i >= 0; i-- {
			if up[a][i] != up[b][i] {
				a = up[a][i]
				b = up[b][i]
			}
		}
		return up[a][0]
	}
	fmt.Println(lca(3, 5), lca(4, 6))
}
