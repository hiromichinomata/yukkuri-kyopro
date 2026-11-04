package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1_000_000_007

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	m := 2 * n
	pair := make([]int, m)
	for i := range pair {
		pair[i] = -1
	}
	for i := 0; i < k; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		pair[a-1], pair[b-1] = b-1, a-1
	}
	g := make([]int, m+1) // 自由な点 x 個を組にする方法の数
	g[0] = 1
	for x := 2; x <= m; x += 2 {
		g[x] = g[x-2] * (x - 1) % mod
	}
	free := make([]int, m+1)
	for i := 0; i < m; i++ {
		free[i+1] = free[i]
		if pair[i] == -1 {
			free[i+1]++
		}
	}
	// dp[l][r]: 区間 [l, r] の点どうしだけで組み、l と r が同じ連結成分になる方法の数
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, m)
	}
	ans, total := 0, free[m]
	for l := 0; l < m; l++ {
		lo, hi := m, -1
		for r := l; r < m; r++ {
			if pair[r] != -1 {
				lo, hi = min(lo, pair[r]), max(hi, pair[r])
			}
			if (r-l)%2 == 0 || lo < l || hi > r {
				continue
			}
			v := g[free[r+1]-free[l]]
			for mid := l + 1; mid < r; mid += 2 {
				if dp[l][mid] != 0 {
					v = (v - dp[l][mid]*g[free[r+1]-free[mid+1]]%mod + mod) % mod
				}
			}
			dp[l][r] = v
			ans = (ans + v*g[total-(free[r+1]-free[l])]) % mod
		}
	}
	fmt.Println(ans)
}
