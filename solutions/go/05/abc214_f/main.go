package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1_000_000_007

func main() {
	in := bufio.NewReader(os.Stdin)
	var s string
	fmt.Fscan(in, &s)
	n := len(s)
	// 同じ文字列 T を二重に数えないため、T を「できるだけ左の位置」で選ぶ選び方だけを数える。
	// dp[i]: 最後に選んだ文字が位置 i（1 始まり）である文字列の数。dp[0] は「まだ何も選んでいない」
	dp := make([]int, n+1)
	dp[0] = 1
	for i := 1; i <= n; i++ {
		c := s[i-1]
		total, ok := 0, true
		// 1 つ前に選んだ位置 p を、i に近い方から見る（隣は選べないので p ≤ i - 2）。
		// p+2〜i-1 に c があると、c をもっと左で選べる → 「できるだけ左」ではないので打ち切る
		for p := i - 2; p >= 1; p-- {
			if p+2 <= i-1 && s[p+1] == c { // p を 1 つ減らすと、位置 p+2 が新たに範囲に入る
				ok = false
				break
			}
			total += dp[p]
		}
		// 何も選んでいない状態から c を選ぶ: 位置 1〜i-1 に c がなければよい
		// （3〜i-1 は上のループで確認済みなので、残りは位置 1 と 2）
		if ok {
			for q := 1; q <= 2 && q <= i-1; q++ {
				if s[q-1] == c {
					ok = false
				}
			}
			if ok {
				total += dp[0]
			}
		}
		dp[i] = total % mod
	}
	ans := 0
	for _, v := range dp[1:] {
		ans = (ans + v) % mod
	}
	fmt.Println(ans)
}
