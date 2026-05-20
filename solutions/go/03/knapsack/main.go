package main

import "fmt"

func knapsack(weights, values []int, cap int) int {
	dp := make([]int, cap+1)
	for i := 0; i < len(weights); i++ {
		w, v := weights[i], values[i]
		for c := cap; c >= w; c-- {
			if dp[c-w]+v > dp[c] {
				dp[c] = dp[c-w] + v
			}
		}
	}
	return dp[cap]
}

func main() {
	fmt.Println(knapsack([]int{2, 3, 4}, []int{3, 4, 5}, 5))
}
