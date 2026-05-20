package main

import "fmt"

const mod = 998244353

func main() {
	n := 10
	c := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		c[i] = make([]int, n+1)
		c[i][0], c[i][i] = 1, 1
		for j := 1; j < i; j++ {
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % mod
		}
	}
	fmt.Println(c[5][2])
}
