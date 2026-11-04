package main

import (
	"bufio"
	"fmt"
	"os"
)

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
	// levels: roots（中心の頂点 1 つ、または中心の辺の両端）から BFS し、
	// 最大の深さと、各深さでの「子の数」の最大値を返す
	levels := func(roots []int) (int, []int) {
		dist := make([]int, n)
		for i := range dist {
			dist[i] = -1
		}
		q := []int{}
		for _, r := range roots {
			dist[r] = 0
			q = append(q, r)
		}
		var mc []int
		maxD := 0
		for h := 0; h < len(q); h++ {
			v := q[h]
			d := dist[v]
			cnt := 0
			for _, to := range g[v] {
				if dist[to] == -1 {
					dist[to] = d + 1
					q = append(q, to)
					cnt++
				}
			}
			for len(mc) <= d {
				mc = append(mc, 0)
			}
			if cnt > mc[d] {
				mc[d] = cnt
			}
			if d > maxD {
				maxD = d
			}
		}
		return maxD, mc
	}
	// 色の数の最小は「直径の半分 + 1」。中心（頂点か辺）から見て同じ深さの子の数を最大にそろえると、
	// 葉の数はその積（辺が中心なら 2 倍）
	bestC, bestL := -1, int64(0)
	consider := func(c int, l int64) {
		if bestC == -1 || c < bestC || (c == bestC && l < bestL) {
			bestC, bestL = c, l
		}
	}
	for c := 0; c < n; c++ {
		d, mc := levels([]int{c})
		leaves := int64(1)
		for _, x := range mc {
			if x > 0 {
				leaves *= int64(x)
			}
		}
		consider(d+1, leaves)
	}
	for u := 0; u < n; u++ {
		for _, v := range g[u] {
			if u < v {
				d, mc := levels([]int{u, v})
				leaves := int64(2)
				for _, x := range mc {
					if x > 0 {
						leaves *= int64(x)
					}
				}
				consider(d+1, leaves)
			}
		}
	}
	fmt.Println(bestC, bestL)
}
