package main

import (
	"bufio"
	"fmt"
	"os"
)

// maxMatching は二部グラフの最大マッチングを増加路 DFS で求める（O(VE)）。
// g[u] は左 u から行ける右の頂点。
func maxMatching(nLeft, nRight int, g [][]int) int {
	matchR := make([]int, nRight) // 右 v の相手（左の番号）、いなければ -1
	for i := range matchR {
		matchR[i] = -1
	}
	var seen []bool
	var try func(u int) bool
	try = func(u int) bool {
		for _, v := range g[u] {
			if seen[v] {
				continue
			}
			seen[v] = true
			// v が空いている、または v の今の相手を別の右頂点に移せるなら u と組める
			if matchR[v] == -1 || try(matchR[v]) {
				matchR[v] = u
				return true
			}
		}
		return false
	}
	result := 0
	for u := 0; u < nLeft; u++ {
		seen = make([]bool, nRight)
		if try(u) {
			result++
		}
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var nLeft, nRight, m int
	fmt.Fscan(in, &nLeft, &nRight, &m)
	g := make([][]int, nLeft)
	for i := 0; i < m; i++ {
		var u, v int
		fmt.Fscan(in, &u, &v)
		g[u] = append(g[u], v)
	}
	fmt.Fprintln(out, maxMatching(nLeft, nRight, g))
}
