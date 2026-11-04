package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n, &m)
	// X と Y を入れ替えても条件は同じ形なので、N ≤ M にそろえて作り、最後に戻す
	swap := n > m
	if swap {
		n, m = m, n
	}
	// 3X + Y が 1 ずつ増えるように「右へ 1」「下へ 1・左へ 2」で進む階段状の道を作ると、
	// X + 3Y も重ならずに上限 3N+M-3（N = M が偶数のときは 1 少ない）を達成できる
	var pts [][2]int
	for x := 1; x <= n; x++ {
		var lo, hi int
		switch {
		case x == n: // 最後の行は右端まで
			lo, hi = n-1, m
			if n%2 == 1 {
				lo = n - 2
			}
		case x%2 == 1:
			lo, hi = x-2, x+2
		default:
			lo, hi = x-1, x+1
		}
		for y := max(1, lo); y <= min(m, hi); y++ {
			if swap {
				pts = append(pts, [2]int{y, x})
			} else {
				pts = append(pts, [2]int{x, y})
			}
		}
	}
	fmt.Fprintln(out, len(pts))
	for _, p := range pts {
		fmt.Fprintln(out, p[0], p[1])
	}
}
