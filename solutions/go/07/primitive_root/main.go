package main

import (
	"bufio"
	"fmt"
	"os"
)

func powMod(a, e, p int) int {
	res := 1
	a %= p
	for e > 0 {
		if e&1 == 1 {
			res = res * a % p
		}
		a = a * a % p
		e >>= 1
	}
	return res
}

func primeFactors(n int) []int {
	res := []int{}
	for p := 2; p*p <= n; p++ {
		if n%p == 0 {
			res = append(res, p)
			for n%p == 0 {
				n /= p
			}
		}
	}
	if n > 1 {
		res = append(res, n)
	}
	return res
}

// primitiveRoot は素数 p の最小の原根を返す。
// g が原根 ⇔ p-1 のすべての素因数 q について g^((p-1)/q) ≠ 1 (mod p)。
func primitiveRoot(p int) int {
	if p == 2 {
		return 1
	}
	qs := primeFactors(p - 1)
	for g := 2; ; g++ {
		ok := true
		for _, q := range qs {
			if powMod(g, (p-1)/q, p) == 1 {
				ok = false
				break
			}
		}
		if ok {
			return g
		}
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var p int
	fmt.Fscan(in, &p)
	fmt.Fprintln(out, primitiveRoot(p))
}
