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

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	m := n - 1 // 機械の数
	fac, inv := make([]int, m+1), make([]int, m+1)
	fac[0] = 1
	for i := 1; i <= m; i++ {
		fac[i] = fac[i-1] * i % mod
	}
	inv[m] = powMod(fac[m], mod-2)
	for i := m; i > 0; i-- {
		inv[i-1] = inv[i] * i % mod
	}
	comb := func(a, b int) int {
		if b < 0 || a < 0 || b > a {
			return 0
		}
		return fac[a] * inv[b] % mod * inv[a-b] % mod
	}
	// f[k]: 最初の k 台で全部塗り終わっている順列の数。
	// 機械 1 と N-1 を含み、使わない m-k 台を使う k 台の間 k-1 か所に 1 台ずつ → C(k-1, m-k)
	f := make([]int, m+1)
	for k := 1; k <= m; k++ {
		f[k] = comb(k-1, m-k) * fac[k] % mod * fac[m-k] % mod
	}
	ans := 0
	for k := 1; k <= m; k++ { // ちょうど k 台目で塗り終わる順列は f[k] - f[k-1] 個
		ans = (ans + k*((f[k]-f[k-1]+mod)%mod)) % mod
	}
	fmt.Println(ans)
}
