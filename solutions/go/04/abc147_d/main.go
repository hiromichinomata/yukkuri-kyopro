package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1_000_000_007

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	ans := 0
	for b := 0; b < 60; b++ { // ビットごとに寄与を数える（主客転倒）
		ones := 0
		for _, x := range a {
			ones += x >> b & 1
		}
		// b ビット目が 1 になる組 = 「1 の数」×「0 の数」。それぞれ 2^b ずつ寄与する
		pairs := ones * (n - ones) % mod
		ans = (ans + pairs*((1<<b)%mod)) % mod
	}
	fmt.Println(ans)
}
