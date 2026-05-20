package main

import "fmt"

func paths(h, w int, blocked [][]bool) int {
	dp := make([][]int, h)
	for i := range dp {
		dp[i] = make([]int, w)
	}
	if !blocked[0][0] {
		dp[0][0] = 1
	}
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if blocked[i][j] {
				dp[i][j] = 0
				continue
			}
			if i > 0 {
				dp[i][j] += dp[i-1][j]
			}
			if j > 0 {
				dp[i][j] += dp[i][j-1]
			}
		}
	}
	return dp[h-1][w-1]
}

func main() {
	blocked := make([][]bool, 3)
	for i := range blocked {
		blocked[i] = make([]bool, 3)
	}
	blocked[1][1] = true
	fmt.Println(paths(3, 3, blocked))
}
