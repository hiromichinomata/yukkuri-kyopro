package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1_000_000_007

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n, &m)
	broken := make([]bool, n+1)
	for i := 0; i < m; i++ {
		var a int
		fmt.Fscan(in, &a)
		broken[a] = true
	}
	dp := make([]int, n+1) // dp[i]: i 段目にたどり着く方法の数
	dp[0] = 1
	for i := 1; i <= n; i++ {
		if broken[i] {
			continue // 壊れた段には乗れない → 0 のまま
		}
		dp[i] = dp[i-1]
		if i >= 2 {
			dp[i] += dp[i-2]
		}
		dp[i] %= mod
	}
	fmt.Fprintln(out, dp[n])
}
