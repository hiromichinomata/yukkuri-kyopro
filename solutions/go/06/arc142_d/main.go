package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 998244353

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	g := make([][]int, n)
	for i := 0; i < n-1; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		g[a-1] = append(g[a-1], b-1)
		g[b-1] = append(g[b-1], a-1)
	}
	// 頂点全体を「2 頂点以上のパス」に分け、パスどうしは「端点どうし」か「内部どうし」の辺でだけつながる。
	// 内部どうしの辺 1 本ごとに向きを独立に選べる（× 2）。
	// up: パスが親へ続く / ce: 部分木内で閉じ v は端点 / ci: 部分木内で閉じ v は内部
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -1
	}
	parent[0] = n
	order := []int{0}
	for h := 0; h < len(order); h++ {
		v := order[h]
		for _, to := range g[v] {
			if parent[to] == -1 {
				parent[to] = v
				order = append(order, to)
			}
		}
	}
	up, ce, ci := make([]int, n), make([]int, n), make([]int, n)
	for k := n - 1; k >= 0; k-- {
		v := order[k]
		e0, e1 := 1, 0
		i0, i1, i2 := 1, 0, 0
		for _, c := range g[v] {
			if c == parent[v] {
				continue
			}
			u, x, y := up[c], ce[c], 2*ci[c]%mod
			e0, e1 = e0*x%mod, (e1*x+e0*u)%mod
			i0, i1, i2 = i0*y%mod, (i1*y+i0*u)%mod, (i2*y+i1*u)%mod
		}
		up[v] = (e0 + i1) % mod
		ce[v] = e1
		ci[v] = i2
	}
	fmt.Println(2 * (ce[0] + ci[0]) % mod)
}
