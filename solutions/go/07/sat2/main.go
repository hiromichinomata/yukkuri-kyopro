package main

import "fmt"

func scc(g [][]int, n int) []int {
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
	return comp
}

func sat2Solvable(implications [][2]int, nVars int) bool {
	n := 2 * nVars
	g := make([][]int, n)
	for _, e := range implications {
		g[e[0]] = append(g[e[0]], e[1])
	}
	comp := scc(g, n)
	for i := 0; i < nVars; i++ {
		if comp[2*i] == comp[2*i+1] {
			return false
		}
	}
	return true
}

func main() {
	nVars := 2
	implications := [][2]int{{1, 2}, {3, 2}}
	fmt.Println(sat2Solvable(implications, nVars))
}
