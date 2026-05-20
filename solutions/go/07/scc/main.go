package main

import "fmt"

func scc(g [][]int, n int) ([]int, int) {
	order := []int{}
	seen := make([]bool, n)
	var dfs func(v int)
	dfs = func(v int) {
		seen[v] = true
		for _, to := range g[v] {
			if !seen[to] {
				dfs(to)
			}
		}
		order = append(order, v)
	}
	for i := 0; i < n; i++ {
		if !seen[i] {
			dfs(i)
		}
	}
	rg := make([][]int, n)
	for v := 0; v < n; v++ {
		for _, to := range g[v] {
			rg[to] = append(rg[to], v)
		}
	}
	comp := make([]int, n)
	for i := range comp {
		comp[i] = -1
	}
	cid := 0
	seen = make([]bool, n)
	var rdfs func(v int)
	rdfs = func(v int) {
		seen[v] = true
		comp[v] = cid
		for _, to := range rg[v] {
			if !seen[to] {
				rdfs(to)
			}
		}
	}
	for i := n - 1; i >= 0; i-- {
		v := order[i]
		if !seen[v] {
			rdfs(v)
			cid++
		}
	}
	return comp, cid
}

func main() {
	n := 5
	g := make([][]int, n)
	edges := [][2]int{{0, 1}, {1, 2}, {2, 0}, {1, 3}, {3, 4}}
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
	}
	comp, k := scc(g, n)
	fmt.Println(k, comp)
}
