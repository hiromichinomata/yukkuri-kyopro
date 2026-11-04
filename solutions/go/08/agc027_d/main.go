package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	if n == 2 {
		fmt.Fprintln(out, "4 7\n23 10") // N = 2 は手で作った例（余りはすべて 3）
		return
	}
	k := n + 2
	var ps []int64 // 小さい順に 2k 個の素数
	for x := int64(2); len(ps) < 2*k; x++ {
		prime := true
		for _, p := range ps {
			if p*p > x {
				break
			}
			if x%p == 0 {
				prime = false
				break
			}
		}
		if prime {
			ps = append(ps, x)
		}
	}
	p1, p2 := ps[:k], ps[k:]
	a := make([][]int64, n)
	for i := range a {
		a[i] = make([]int64, n)
	}
	// 白マス (i + j が偶数) に 2 方向の対角線の素数の積、黒マスに隣の最小公倍数 + 1（余りはすべて 1）
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if (i+j)%2 == 0 {
				a[i][j] = p1[(i+j)/2] * p2[(i-j+n)/2]
			}
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if (i+j)%2 == 1 {
				l := int64(1)
				for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
					x, y := i+d[0], j+d[1]
					if 0 <= x && x < n && 0 <= y && y < n {
						l = l / gcd(l, a[x][y]) * a[x][y]
					}
				}
				a[i][j] = l + 1
			}
		}
	}
	for _, row := range a {
		for j, v := range row {
			if j > 0 {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, v)
		}
		fmt.Fprintln(out)
	}
}
