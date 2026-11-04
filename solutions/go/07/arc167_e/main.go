package main

import (
	"bufio"
	"fmt"
	"os"
)

// inv は q の mod p での逆元（拡張ユークリッド）
func inv(q, p int) int {
	a, b, x0, x1 := q%p, p, 1, 0
	for b != 0 {
		t := a / b
		a, b = b, a-t*b
		x0, x1 = x1, x0-t*x1
	}
	return (x0%p + p) % p
}

// build は面積 S/2 で単位正方形をちょうど 1 つ含む三角形。なければ ok = false
func build(s int) (tri [6]int, ok bool) {
	switch s {
	case 1, 2, 3, 5, 7: // 小さい S は作れない
		return tri, false
	case 4:
		return [6]int{1, 1, 1, 3, 3, 3}, true
	}
	t := s - 1
	var p, q int // p + q + 1 = S となる互いに素な p, q ≥ 2
	switch {
	case t%2 == 1:
		p, q = 2, t-2
	case (t/2)%2 == 0:
		p, q = t/2-1, t/2+1
	default:
		p, q = t/2-2, t/2+2
	}
	sp := inv(q, p) // s' q - t' p = 1
	tp := (sp*q - 1) / p
	return [6]int{0, 0, p, q, sp + 1, tp - 1}, true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var s int
		fmt.Fscan(in, &s)
		tri, ok := build(s)
		if !ok {
			fmt.Fprintln(out, "No")
			continue
		}
		fmt.Fprintln(out, "Yes")
		fmt.Fprintln(out, tri[0], tri[1], tri[2], tri[3], tri[4], tri[5])
	}
}
