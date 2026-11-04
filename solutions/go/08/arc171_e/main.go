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

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, a, b int
	fmt.Fscan(in, &n, &m, &a, &b)
	// 白石は「隣り合う 2 行の組」K 個と「隣り合う 2 列の組」K 個に並ぶ（M = 2K）。
	// 最後に訪れる組は黒石の行（列）を含み、その直前の組は黒石が戻ってくる側になければならない
	if m%2 == 1 || m < 4 {
		fmt.Println(0)
		return
	}
	k := m / 2
	fac, inv := make([]int, n+1), make([]int, n+1)
	fac[0] = 1
	for i := 1; i <= n; i++ {
		fac[i] = fac[i-1] * i % mod
	}
	inv[n] = powMod(fac[n], mod-2)
	for i := n; i > 0; i-- {
		inv[i-1] = inv[i] * i % mod
	}
	comb := func(x, y int) int {
		if y < 0 || x < y || x < 0 {
			return 0
		}
		return fac[x] * inv[y] % mod * inv[x-y] % mod
	}
	// sideSum: 長さ l（直前の組が来る側）と r の 2 区間から組を合計 j 個選ぶ方法を、l 側の組の数で重みづけ
	sideSum := func(l, r, j int) int {
		s := 0
		for i := 1; i <= j; i++ {
			s = (s + i*comb(l-i, i)%mod*comb(r-(j-i), j-i)) % mod
		}
		return s
	}
	countLine := func(x int) int {
		tot := 0
		if x-1 >= 1 { // 組 {x-1, x}: 直前の組は 1..x-2 にある
			tot += sideSum(x-2, n-x, k-1)
		}
		if x+1 <= n { // 組 {x, x+1}: 直前の組は x+2..n にある
			tot += sideSum(n-x-1, x-1, k-1)
		}
		return tot % mod * fac[k-2] % mod
	}
	fmt.Println(2 * countLine(a) % mod * countLine(b) % mod) // 縦から始めるか横からかで 2 倍
}
