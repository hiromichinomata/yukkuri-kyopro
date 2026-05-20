package main

import "fmt"

func dfs(v int, g [][]int, seen []bool) {
	seen[v] = true
	for _, to := range g[v] {
		if !seen[to] {
			dfs(to, g, seen)
		}
	}
}

func main() {
	// 0 — 1,2 の木で DFS（例）
	g := [][]int{{1, 2}, {}, {}}
	seen := make([]bool, 3)
	dfs(0, g, seen)
	fmt.Println(seen)
}
