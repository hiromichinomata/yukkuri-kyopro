package main

import "fmt"

const mod = 998244353

func modPow(a, e int) int {
	res := 1
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
	n := 10
	fac := make([]int, n+1)
	inv := make([]int, n+1)
	fac[0] = 1
	for i := 1; i <= n; i++ {
		fac[i] = fac[i-1] * i % mod
	}
	inv[n] = modPow(fac[n], mod-2)
	for i := n; i > 0; i-- {
		inv[i-1] = inv[i] * i % mod
	}
	ncr := fac[5] * inv[2] % mod * inv[3] % mod
	fmt.Println(ncr)
}
