package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 998244353

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, q int
	fmt.Fscan(in, &n, &q)
	a := make([]int, 1<<n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	// 1 回の操作は、ビット X が違うだけの 2 つ組に 2×2 行列を掛けることと同じ。
	// 違うビットの操作は順番を入れ替えても同じなので、ビットごとに行列をまとめて掛ける
	mats := make([][4]int, n) // [[p, q], [r, s]]
	for x := range mats {
		mats[x] = [4]int{1, 0, 0, 1}
	}
	for i := 0; i < q; i++ {
		var x, y int
		fmt.Fscan(in, &x, &y)
		m := mats[x]
		if y == 0 { // 下の行に上の行を足す
			mats[x] = [4]int{m[0], m[1], (m[2] + m[0]) % mod, (m[3] + m[1]) % mod}
		} else { // 上の行に下の行を足す
			mats[x] = [4]int{(m[0] + m[2]) % mod, (m[1] + m[3]) % mod, m[2], m[3]}
		}
	}
	for x := 0; x < n; x++ {
		m := mats[x]
		step := 1 << x
		for base := 0; base < 1<<n; base += step << 1 {
			for j := base; j < base+step; j++ {
				a0, a1 := a[j], a[j+step]
				a[j] = (m[0]*a0 + m[1]*a1) % mod
				a[j+step] = (m[2]*a0 + m[3]*a1) % mod
			}
		}
	}
	for i, v := range a {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, v)
	}
	fmt.Fprintln(out)
}
