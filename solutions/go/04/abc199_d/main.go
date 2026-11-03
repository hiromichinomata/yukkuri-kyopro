package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	g := make([][]int, n)
	for i := 0; i < m; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		g[a-1] = append(g[a-1], b-1)
		g[b-1] = append(g[b-1], a-1)
	}
	color := make([]int, n)
	for i := range color {
		color[i] = -1
	}
	ans := 1
	for s := 0; s < n; s++ {
		if color[s] != -1 {
			continue
		}
		// 連結成分の頂点を DFS 順に並べる（どの頂点も、先に並んだ頂点のどれかと隣り合う）
		order, stack := []int{}, []int{s}
		color[s] = 0
		for len(stack) > 0 {
			v := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			order = append(order, v)
			for _, to := range g[v] {
				if color[to] == -1 {
					color[to] = 0
					stack = append(stack, to)
				}
			}
		}
		for _, v := range order {
			color[v] = -1
		}
		var count func(i int) int
		count = func(i int) int {
			if i == len(order) {
				return 1
			}
			v := order[i]
			total := 0
			for c := 0; c < 3; c++ {
				ok := true
				for _, to := range g[v] {
					if color[to] == c {
						ok = false
						break
					}
				}
				if ok {
					color[v] = c
					total += count(i + 1)
					color[v] = -1
				}
			}
			return total
		}
		// 先頭の頂点の色は 3 通りとも対称なので、0 に固定して 3 倍する
		color[order[0]] = 0
		ways := count(1) * 3
		for _, v := range order {
			color[v] = 3 // 塗り終わった成分は「どの色とも違う」扱いにしておく
		}
		ans *= ways
	}
	fmt.Println(ans)
}
