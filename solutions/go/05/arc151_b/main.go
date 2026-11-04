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
	var n, m int
	fmt.Fscan(in, &n, &m)
	p := make([]int, n)
	for i := range p {
		fmt.Fscan(in, &p[i])
		p[i]--
	}
	// 置換 P のサイクルの数 c を数える（i と P_i を Union-Find でつないだ連結成分の数と同じ）
	seen := make([]bool, n)
	c := 0
	for i := 0; i < n; i++ {
		if !seen[i] {
			c++
			for j := i; !seen[j]; j = p[j] {
				seen[j] = true
			}
		}
	}
	// A = A∘P になるのは M^c 通り。残りは「A < A∘P」と「A > A∘P」に半分ずつ分かれる（対称性）
	ans := (powMod(m, n) - powMod(m, c) + mod) % mod * powMod(2, mod-2) % mod
	fmt.Println(ans)
}
