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

	var h, w, n int
	fmt.Fscan(in, &h, &w, &n)
	// 差分は 1 マス大きく取る（右端・下端の +1 が溢れないように）
	d := make([][]int, h+1)
	for i := range d {
		d[i] = make([]int, w+1)
	}
	for k := 0; k < n; k++ {
		// 矩形 [r1, r2) × [c1, c2) に +1（0-indexed、右端・下端は含まない）
		var r1, c1, r2, c2 int
		fmt.Fscan(in, &r1, &c1, &r2, &c2)
		d[r1][c1]++
		d[r1][c2]--
		d[r2][c1]--
		d[r2][c2]++
	}
	// 横方向に累積 → 縦方向に累積
	for i := 0; i <= h; i++ {
		for j := 1; j <= w; j++ {
			d[i][j] += d[i][j-1]
		}
	}
	for i := 1; i <= h; i++ {
		for j := 0; j <= w; j++ {
			d[i][j] += d[i-1][j]
		}
	}
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if j > 0 {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, d[i][j])
		}
		fmt.Fprintln(out)
	}
}
