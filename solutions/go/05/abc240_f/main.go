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

	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var n, m int
		fmt.Fscan(in, &n, &m)
		a, b := 0, 0 // 直前までの A と B（A_0 = B_0 = 0）
		best, first := 0, true
		for i := 0; i < n; i++ {
			var x, y int
			fmt.Fscan(in, &x, &y)
			// この区間で k 個進んだとき: B_k = b + x k、A_k = a + b k + x k(k+1)/2（k = 1〜y）
			cand := []int{1, y}
			// A は B_k > 0 の間だけ増える。x < 0 なら B_k が正である最後の k で A が最大
			if x < 0 && b > 0 {
				if k := b / -x; 1 <= k && k <= y {
					cand = append(cand, k)
				}
			}
			for _, k := range cand {
				v := a + b*k + x*k*(k+1)/2
				if first || v > best {
					best, first = v, false
				}
			}
			a += b*y + x*y*(y+1)/2
			b += x * y
		}
		fmt.Fprintln(out, best)
	}
}
