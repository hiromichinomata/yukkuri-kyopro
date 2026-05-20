package main

import "fmt"

func dfs(v, parent int, g [][]int, dp []int) {
	dp[v] = 1
	for _, to := range g[v] {
		if to == parent {
			continue
		}
		dfs(to, v, g, dp)
		dp[v] += dp[to]
	}
}

func main() {
	g := [][]int{{1, 2}, {0, 3}, {0}, {1}}
	dp := make([]int, 4)
	dfs(0, -1, g, dp)
	fmt.Println(dp)
}
