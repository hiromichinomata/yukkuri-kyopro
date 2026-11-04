package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 998244353

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

func solve(n, p100 int) int {
	p := p100 * powMod(100, mod-2) % mod
	c := (2*p - 1 + mod) % mod // 「同じ向きが続く確率 − 向きが変わる確率」
	m := (n - 1) % mod
	// E = Σ_{d=0}^{N-2} (N-1-d)(1 + c^d)/2、Σ_{d=0}^{m-1} (m-d) c^d = (m - c(1-c^m)/(1-c)) / (1-c)
	inv1c := powMod((1-c+mod)%mod, mod-2)
	cm := powMod(c, n-1) // 指数はそのまま（N ≤ 10^18 なので int64 に収まる）
	geo := (m - c*((1-cm+mod)%mod)%mod*inv1c%mod + mod) % mod * inv1c % mod
	inv2 := powMod(2, mod-2)
	tri := m * ((m + 1) % mod) % mod * inv2 % mod
	return (tri + geo) % mod * inv2 % mod
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var n, p int
		fmt.Fscan(in, &n, &p)
		fmt.Fprintln(out, solve(n, p))
	}
}
