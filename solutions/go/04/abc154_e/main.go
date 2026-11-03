package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var s string
	var k int
	fmt.Fscan(in, &s, &k)
	// dp[tight][c]: 上の桁から決めて、0 でない桁を c 個使った数の個数
	// tight = 1 は「ここまで N と同じ」、0 は「すでに N より小さい」
	dp := [2][5]int{}
	dp[1][0] = 1
	for _, ch := range s {
		d := int(ch - '0')
		ndp := [2][5]int{}
		for tight := 0; tight < 2; tight++ {
			for c := 0; c <= k; c++ {
				if dp[tight][c] == 0 {
					continue
				}
				limit := 9
				if tight == 1 {
					limit = d
				}
				for x := 0; x <= limit; x++ {
					nt := 0
					if tight == 1 && x == limit {
						nt = 1
					}
					nc := c
					if x != 0 {
						nc++
					}
					if nc > k {
						nc = k + 1 // K を超えたら k+1 にまとめる
					}
					ndp[nt][nc] += dp[tight][c]
				}
			}
		}
		dp = ndp
	}
	fmt.Println(dp[0][k] + dp[1][k])
}
