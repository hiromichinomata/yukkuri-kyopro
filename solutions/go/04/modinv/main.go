package main

import "fmt"

const mod = 998244353

func modPow(a, e int) int {
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

// prepareFac は 0!〜n! と、その逆元を作る（フェルマーの小定理で n! の逆元を 1 回だけ求める）
func prepareFac(n int) (fac, inv []int) {
	fac = make([]int, n+1)
	inv = make([]int, n+1)
	fac[0] = 1
	for i := 1; i <= n; i++ {
		fac[i] = fac[i-1] * i % mod
	}
	inv[n] = modPow(fac[n], mod-2)
	for i := n; i > 0; i-- {
		inv[i-1] = inv[i] * i % mod
	}
	return
}

func ncr(n, r int, fac, inv []int) int {
	if r < 0 || r > n {
		return 0
	}
	return fac[n] * inv[r] % mod * inv[n-r] % mod
}

func main() {
	fac, inv := prepareFac(10)
	fmt.Println(ncr(5, 2, fac, inv))
}
