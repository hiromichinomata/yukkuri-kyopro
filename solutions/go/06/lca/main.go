package main

import "fmt"

func dfs(v, p int, depth []int, up [][]int, g [][]int, LOG int) {
	up[v][0] = p
	for i := 1; i < LOG; i++ {
		if up[v][i-1] != -1 {
			up[v][i] = up[up[v][i-1]][i-1]
		} else {
			up[v][i] = -1
		}
	}
	for _, to := range g[v] {
		if to == p {
			continue
		}
		depth[to] = depth[v] + 1
		dfs(to, v, depth, up, g, LOG)
	}
}

func lca(a, b int, depth []int, up [][]int, LOG int) int {
	if depth[a] < depth[b] {
		a, b = b, a
	}
	d := depth[a] - depth[b]
	for i := 0; i < LOG; i++ { // 深い方を、深さの差だけ上げる
		if d>>i&1 == 1 {
			a = up[a][i]
		}
	}
	if a == b {
		return a
	}
	for i := LOG - 1; i >= 0; i-- { // 祖先が分かれる直前まで一緒に上げる
		if up[a][i] != up[b][i] {
			a = up[a][i]
			b = up[b][i]
		}
	}
	return up[a][0]
}

func buildLCA(g [][]int, root int) ([]int, [][]int, int) {
	n := len(g)
	LOG := 1
	for 1<<LOG <= n { // 2^LOG > n なので、深さの差（< n）を表せる
		LOG++
	}
	up := make([][]int, n)
	for i := range up {
		up[i] = make([]int, LOG)
	}
	depth := make([]int, n)
	dfs(root, -1, depth, up, g, LOG)
	return depth, up, LOG
}

func main() {
	n := 7
	g := make([][]int, n)
	for _, e := range [][2]int{{0, 1}, {0, 2}, {1, 3}, {1, 4}, {2, 5}, {2, 6}} {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	depth, up, LOG := buildLCA(g, 0)
	fmt.Println(lca(3, 5, depth, up, LOG), lca(4, 6, depth, up, LOG))
}
