package main

import (
	"bufio"
	"fmt"
	"os"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	x, y, z := make([]int, n), make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &x[i], &y[i], &z[i])
	}
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			up := z[j] - z[i]
			if up < 0 {
				up = 0
			}
			dist[i][j] = abs(x[j]-x[i]) + abs(y[j]-y[i]) + up
		}
	}
	// この費用は三角不等式を満たすので、各都市をちょうど 1 回ずつ回る巡回でよい（巡回セールスマン）
	const inf = 1 << 60
	dp := make([][]int, 1<<n) // dp[mask][v]: 訪れた都市の集合 mask、いま v にいるときの最小費用
	for i := range dp {
		dp[i] = make([]int, n)
		for j := range dp[i] {
			dp[i][j] = inf
		}
	}
	dp[1][0] = 0
	for mask := 0; mask < 1<<n; mask++ {
		for v := 0; v < n; v++ {
			cur := dp[mask][v]
			if cur == inf {
				continue
			}
			for to := 0; to < n; to++ {
				if mask>>to&1 == 1 {
					continue
				}
				nm := mask | 1<<to
				if cur+dist[v][to] < dp[nm][to] {
					dp[nm][to] = cur + dist[v][to]
				}
			}
		}
	}
	full := 1<<n - 1
	ans := inf
	for v := 0; v < n; v++ {
		if c := dp[full][v] + dist[v][0]; c < ans {
			ans = c
		}
	}
	fmt.Println(ans)
}
