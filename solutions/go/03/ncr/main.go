package main

import "fmt"

const mod = 998244353

// buildNCR はパスカルの三角形で c[i][j] = iCj (mod) を作る
func buildNCR(n int) [][]int {
	c := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		c[i] = make([]int, n+1)
	}
	c[0][0] = 1
	for i := 1; i <= n; i++ {
		c[i][0], c[i][i] = 1, 1
		for j := 1; j < i; j++ {
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % mod
		}
	}
	return c
}

func main() {
	c := buildNCR(10)
	fmt.Println(c[5][2])
}
