package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1_000_000_007

func powMod(a, e int) int {
	res := 1
	a %= mod
	for e > 0 {
		if e&1 == 1 {
			res = res * a % mod
		}
		a = a * a % mod
		e >>= 1
	}
	return res
}

// comb は n が大きく r が小さいとき: n(n-1)…(n-r+1) / r! を mod で計算
func comb(n, r int) int {
	num, den := 1, 1
	for i := 0; i < r; i++ {
		num = num * ((n - i) % mod) % mod
		den = den * (i + 1) % mod
	}
	return num * powMod(den, mod-2) % mod
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, a, b int
	fmt.Fscan(in, &n, &a, &b)
	// 1 本以上の選び方 2^n - 1 から、a 本・b 本の選び方を引く
	ans := (powMod(2, n) - 1 - comb(n, a) - comb(n, b)) % mod
	ans = (ans + 2*mod) % mod
	fmt.Println(ans)
}
