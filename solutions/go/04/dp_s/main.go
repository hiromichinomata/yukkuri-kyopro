package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1_000_000_007

func main() {
	in := bufio.NewReader(os.Stdin)
	var k string
	var d int
	fmt.Fscan(in, &k, &d)
	// dp[tight][r]: 上の桁から決めて、桁和を D で割った余りが r の数の個数
	dp := [2][]int{make([]int, d), make([]int, d)}
	dp[1][0] = 1
	for _, ch := range k {
		lim := int(ch - '0')
		ndp := [2][]int{make([]int, d), make([]int, d)}
		for r := 0; r < d; r++ {
			if free := dp[0][r]; free != 0 {
				for x := 0; x < 10; x++ { // すでに K より小さい → 0〜9 を自由に置ける
					nr := (r + x) % d
					ndp[0][nr] = (ndp[0][nr] + free) % mod
				}
			}
			if tight := dp[1][r]; tight != 0 {
				for x := 0; x <= lim; x++ {
					nr := (r + x) % d
					nt := 0
					if x == lim {
						nt = 1
					}
					ndp[nt][nr] = (ndp[nt][nr] + tight) % mod
				}
			}
		}
		dp = ndp
	}
	// 0〜K のうち桁和が D の倍数のもの。0 自身を除く
	fmt.Println((dp[0][0] + dp[1][0] - 1 + mod) % mod)
}
