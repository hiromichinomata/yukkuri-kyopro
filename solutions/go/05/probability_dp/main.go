package main

import "fmt"

func probReach(n, maxFace int) float64 {
	dp := make([]float64, n+1)
	dp[0] = 1.0
	for i := 0; i < n; i++ {
		for f := 1; f <= maxFace; f++ {
			if i+f <= n {
				dp[i+f] += dp[i] / float64(maxFace)
			}
		}
	}
	return dp[n]
}

func main() {
	fmt.Printf("%.6f\n", probReach(6, 6))
}
