package main

import "fmt"

func mergeStones(a []int) int {
	n := len(a)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for length := 2; length <= n; length++ {
		for l := 0; l+length-1 < n; l++ {
			r := l + length - 1
			dp[l][r] = 1 << 60
			sum := 0
			for k := l; k <= r; k++ {
				sum += a[k]
			}
			for k := l; k < r; k++ {
				if dp[l][k]+dp[k+1][r] < dp[l][r] {
					dp[l][r] = dp[l][k] + dp[k+1][r]
				}
			}
			dp[l][r] += sum
		}
	}
	return dp[0][n-1]
}

func main() {
	fmt.Println(mergeStones([]int{4, 1, 2, 3}))
}
