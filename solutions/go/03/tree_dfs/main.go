package main

import "fmt"

func dfs(v, parent int, g [][]int, depth []int) {
	if parent == -1 {
		depth[v] = 0
	} else {
		depth[v] = depth[parent] + 1
	}
	for _, to := range g[v] {
		if to == parent {
			continue
		}
		dfs(to, v, g, depth)
	}
}

func main() {
	g := [][]int{{1, 2}, {0, 3}, {0}, {1}}
	depth := make([]int, 4)
	dfs(0, -1, g, depth)
	fmt.Println(depth)
}
