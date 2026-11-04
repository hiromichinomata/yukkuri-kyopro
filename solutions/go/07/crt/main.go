package main

import (
	"bufio"
	"fmt"
	"os"
)

// extGcd は a*x + b*y = g = gcd(a, b) となる (g, x, y) を返す。
func extGcd(a, b int) (int, int, int) {
	if b == 0 {
		return a, 1, 0
	}
	g, x, y := extGcd(b, a%b)
	return g, y, x - (a/b)*y
}

func floorMod(a, m int) int {
	a %= m
	if a < 0 {
		a += m
	}
	return a
}

// crt は x ≡ rs[i] (mod ms[i]) をすべて満たす x と lcm を返す。解なしなら lcm = -1。
// 法どうしが互いに素でなくてもよい。lcm が int64 を超える入力は想定しない。
func crt(rs, ms []int) (int, int) {
	r0, m0 := 0, 1
	for i := range rs {
		r1, m1 := floorMod(rs[i], ms[i]), ms[i]
		// x = r0 + m0 * t として、m0 * t ≡ r1 - r0 (mod m1) を解く
		g, p, _ := extGcd(m0, m1)
		if (r1-r0)%g != 0 {
			return 0, -1 // 矛盾（解なし）
		}
		t := floorMod((r1-r0)/g*p, m1/g)
		r0 += m0 * t
		m0 = m0 / g * m1
		r0 = floorMod(r0, m0)
	}
	return r0, m0
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	rs, ms := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &rs[i], &ms[i])
	}
	x, lcm := crt(rs, ms)
	if lcm == -1 {
		fmt.Fprintln(out, -1)
	} else {
		fmt.Fprintln(out, x, lcm)
	}
}
