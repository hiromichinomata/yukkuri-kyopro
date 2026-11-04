package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1_000_000_007

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	m := 2 * n
	a := make([]int, m)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	kind := make([]int, m+1) // 0: A に出てこない値、1: 片方だけ決まった組の値、2: 両方決まった組の値
	c := 0
	for i := 0; i < n; i++ {
		x, y := a[2*i], a[2*i+1]
		switch {
		case x != -1 && y != -1:
			kind[x], kind[y] = 2, 2
		case x == -1 && y == -1:
			c++
		default:
			kind[max(x, y)] = 1
		}
	}
	// 値の大きい方から、j: A に出てこない値で相手待ち、k: 片方決まった組の値で相手待ち
	newDP := func() [][]int {
		d := make([][]int, m+2)
		for i := range d {
			d[i] = make([]int, m+2)
		}
		return d
	}
	dp := newDP()
	dp[0][0] = 1
	for v := m; v >= 1; v-- {
		if kind[v] == 2 {
			continue
		}
		ndp := newDP()
		for j := 0; j <= m; j++ {
			for k := 0; k <= m; k++ {
				x := dp[j][k]
				if x == 0 {
					continue
				}
				if kind[v] == 0 {
					ndp[j+1][k] = (ndp[j+1][k] + x) % mod
					if j > 0 {
						ndp[j-1][k] = (ndp[j-1][k] + x) % mod
					}
					if k > 0 {
						ndp[j][k-1] = (ndp[j][k-1] + x*k) % mod
					}
				} else {
					ndp[j][k+1] = (ndp[j][k+1] + x) % mod
					if j > 0 {
						ndp[j-1][k] = (ndp[j-1][k] + x) % mod
					}
				}
			}
		}
		dp = ndp
	}
	ans := dp[0][0]
	for i := 1; i <= c; i++ { // 両方 -1 の組どうしの区別
		ans = ans * i % mod
	}
	fmt.Println(ans)
}
