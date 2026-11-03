package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1_000_000_007

// countDigitSumMultiple は 1 以上 K 以下で、各桁の和が D の倍数になる整数の個数を返す。
func countDigitSumMultiple(k string, d int) int {
	// dp[tight][r]: 上の桁から決めてきて、桁和 mod D が r の個数
	//   tight=1: ここまで K と完全に一致 / tight=0: すでに K より小さい
	newTable := func() [2][]int { return [2][]int{make([]int, d), make([]int, d)} }
	dp := newTable()
	dp[1][0] = 1
	for _, ch := range k {
		x := int(ch - '0')
		ndp := newTable()
		for tight := 0; tight < 2; tight++ {
			for r := 0; r < d; r++ {
				cur := dp[tight][r]
				if cur == 0 {
					continue
				}
				limit := 9
				if tight == 1 {
					limit = x
				}
				for digit := 0; digit <= limit; digit++ {
					nt := 0
					if tight == 1 && digit == limit {
						nt = 1
					}
					nr := (r + digit) % d
					ndp[nt][nr] = (ndp[nt][nr] + cur) % mod
				}
			}
		}
		dp = ndp
	}
	// 0 も「桁和 0」で数えてしまっているので 1 引く
	return (dp[0][0] + dp[1][0] - 1 + mod) % mod
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var k string
	var d int
	fmt.Fscan(in, &k, &d)
	fmt.Fprintln(out, countDigitSumMultiple(k, d))
}
