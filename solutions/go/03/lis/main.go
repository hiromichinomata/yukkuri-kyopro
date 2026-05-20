package main

import "fmt"

func lis(a []int) int {
	n := len(a)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = 1
	}
	ans := 0
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if a[j] < a[i] && dp[j]+1 > dp[i] {
				dp[i] = dp[j] + 1
			}
		}
		if dp[i] > ans {
			ans = dp[i]
		}
	}
	return ans
}

func main() {
	fmt.Println(lis([]int{3, 1, 4, 2, 5}))
}
