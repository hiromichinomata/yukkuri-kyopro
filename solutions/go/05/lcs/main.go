package main

import "fmt"

func lcs(s, t string) int {
	n, m := len(s), len(t)
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, m+1)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if s[i] == t[j] {
				dp[i+1][j+1] = dp[i][j] + 1
			} else if dp[i+1][j] > dp[i][j+1] {
				dp[i+1][j+1] = dp[i+1][j]
			} else {
				dp[i+1][j+1] = dp[i][j+1]
			}
		}
	}
	return dp[n][m]
}

func main() {
	fmt.Println(lcs("abcde", "ace"))
}
