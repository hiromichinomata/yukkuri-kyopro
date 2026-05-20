package main

import "fmt"

func tsp(dist [][]int, n int) int {
	const INF = 1 << 60
	dp := make([][]int, 1<<n)
	for i := range dp {
		dp[i] = make([]int, n)
		for j := range dp[i] {
			dp[i][j] = INF
		}
	}
	dp[1][0] = 0
	for mask := 0; mask < 1<<n; mask++ {
		for i := 0; i < n; i++ {
			if dp[mask][i] >= INF {
				continue
			}
			for j := 0; j < n; j++ {
				if mask>>j&1 == 1 {
					continue
				}
				nmask := mask | (1 << j)
				if nd := dp[mask][i] + dist[i][j]; nd < dp[nmask][j] {
					dp[nmask][j] = nd
				}
			}
		}
	}
	full := (1 << n) - 1
	ans := INF
	for i := 0; i < n; i++ {
		if dp[full][i] < ans {
			ans = dp[full][i]
		}
	}
	return ans
}

func main() {
	dist := [][]int{{0, 2, 9}, {2, 0, 6}, {9, 6, 0}}
	fmt.Println(tsp(dist, 3))
}
