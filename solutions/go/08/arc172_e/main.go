package main

import (
	"bufio"
	"fmt"
	"os"
)

func powMod(a, e, m int) int {
	res := 1 % m
	a %= m
	for e > 0 {
		if e&1 == 1 {
			res = res * a % m
		}
		a = a * a % m
		e >>= 1
	}
	return res
}

// solve: k ≥ 2 では n^n mod 10^k は n mod 10^k だけで決まるので、mod 100 から 1 桁ずつ伸ばす
func solve(x int) int {
	var cands []int
	for n := 1; n <= 100; n++ {
		if powMod(n, n, 100) == x%100 {
			cands = append(cands, n)
		}
	}
	m := 100
	for step := 0; step < 7; step++ {
		nm := m * 10
		var nxt []int
		for _, c := range cands {
			for d := 0; d < 10; d++ {
				n := c + d*m
				if n > 0 && powMod(n, n, nm) == x%nm {
					nxt = append(nxt, n)
				}
			}
		}
		cands, m = nxt, nm
	}
	best := -1
	for _, c := range cands {
		if best == -1 || c < best {
			best = c
		}
	}
	return best
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var q int
	fmt.Fscan(in, &q)
	for ; q > 0; q-- {
		var x int
		fmt.Fscan(in, &x)
		fmt.Fprintln(out, solve(x))
	}
}
