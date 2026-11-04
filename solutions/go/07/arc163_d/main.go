package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 998244353

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	e := n * (n - 1) / 2
	c := make([][]int, e+1) // 二項係数
	for i := range c {
		c[i] = make([]int, e+1)
		c[i][0] = 1
		for j := 1; j <= i; j++ {
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % mod
		}
	}
	// 強連結成分の数 = 「すべての辺が A から B へ向く」分割 (A, B)（A は空でない）の数。
	// dp[a][x]: 番号順に振り分けて A に a 個、A→B の辺のうち小→大のものが x 本
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, e+1)
	}
	dp[0][0] = 1
	for i := 0; i < n; i++ {
		ndp := make([][]int, n+1)
		for a := range ndp {
			ndp[a] = make([]int, e+1)
		}
		for a := 0; a <= i; a++ {
			for x := 0; x <= e; x++ {
				v := dp[a][x]
				if v == 0 {
					continue
				}
				ndp[a+1][x] = (ndp[a+1][x] + v) % mod // A へ
				if x+a <= e {
					ndp[a][x+a] = (ndp[a][x+a] + v) % mod // B へ（小→大の辺が a 本増える）
				}
			}
		}
		dp = ndp
	}
	ans := 0
	for a := 1; a <= n; a++ {
		inner := a*(a-1)/2 + (n-a)*(n-a-1)/2 // A・B の内側の辺は向きが自由
		for x := 0; x <= e; x++ {
			if dp[a][x] != 0 && m-x >= 0 && m-x <= inner {
				ans = (ans + dp[a][x]*c[inner][m-x]) % mod
			}
		}
	}
	fmt.Println(ans)
}
