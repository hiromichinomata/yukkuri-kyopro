package main

import (
	"bufio"
	"fmt"
	"os"
)

// coloring: 距離の 2 乗が d の 2 点を、必ず違う色（0/1）に塗る塗り方
func coloring(d int) func(x, y int) int {
	t := 0
	for d%4 == 0 { // d = 4^t × r（r は 4 で割り切れない）
		d /= 4
		t++
	}
	if d%2 == 1 {
		// dx^2 + dy^2 が奇数 → (dx + dy) が奇数。市松模様で色が変わる
		return func(x, y int) int { return ((x >> t) + (y >> t)) & 1 }
	}
	// d ≡ 2 (mod 4) → dx, dy はともに奇数。x の偶奇で色が変わる
	return func(x, y int) int { return (x >> t) & 1 }
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, d1, d2 int
	fmt.Fscan(in, &n, &d1, &d2)
	c1, c2 := coloring(d1), coloring(d2)
	var groups [4][][2]int
	for x := 0; x < 2*n; x++ {
		for y := 0; y < 2*n; y++ {
			g := c1(x, y)*2 + c2(x, y)
			groups[g] = append(groups[g], [2]int{x, y})
		}
	}
	// 4N^2 個の点を 4 グループに分けたので、どれかは N^2 個以上ある（鳩の巣原理）
	best := 0
	for g := 1; g < 4; g++ {
		if len(groups[g]) > len(groups[best]) {
			best = g
		}
	}
	for _, p := range groups[best][:n*n] {
		fmt.Fprintln(out, p[0], p[1])
	}
}
