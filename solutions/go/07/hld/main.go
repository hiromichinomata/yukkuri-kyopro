package main

import (
	"bufio"
	"fmt"
	"os"
)

func dfsSize(v, p int, g [][]int, size, parent, depth []int) {
	size[v] = 1
	parent[v] = p
	for _, to := range g[v] {
		if to == p {
			continue
		}
		depth[to] = depth[v] + 1
		dfsSize(to, v, g, size, parent, depth)
		size[v] += size[to]
	}
}

// dfsHLD: h は v が属する重い鎖の先頭。pos は鎖が連続するように振った番号
func dfsHLD(v, p, h int, g [][]int, size, head, pos []int, cur *int) {
	head[v] = h
	pos[v] = *cur
	*cur++
	heavy := -1
	for _, to := range g[v] {
		if to == p {
			continue
		}
		if heavy == -1 || size[to] > size[heavy] {
			heavy = to
		}
	}
	if heavy != -1 {
		dfsHLD(heavy, v, h, g, size, head, pos, cur) // 重い子は同じ鎖
	}
	for _, to := range g[v] {
		if to != p && to != heavy {
			dfsHLD(to, v, to, g, size, head, pos, cur) // 軽い子は新しい鎖の先頭
		}
	}
}

func buildHLD(g [][]int, root int) (parent, depth, head, pos []int) {
	n := len(g)
	size := make([]int, n)
	parent, depth = make([]int, n), make([]int, n)
	head, pos = make([]int, n), make([]int, n)
	cur := 0
	dfsSize(root, -1, g, size, parent, depth)
	dfsHLD(root, -1, root, g, size, head, pos, &cur)
	return
}

func hldLCA(a, b int, parent, depth, head []int) int {
	for head[a] != head[b] { // 鎖の先頭が深い方を、鎖ごと飛ばして上げる
		if depth[head[a]] > depth[head[b]] {
			a = parent[head[a]]
		} else {
			b = parent[head[b]]
		}
	}
	if depth[a] < depth[b] {
		return a
	}
	return b
}

func printInts(out *bufio.Writer, xs []int) {
	for i, x := range xs {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, x)
	}
	fmt.Fprintln(out)
}

func main() {
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	n := 7
	g := make([][]int, n)
	for _, e := range [][2]int{{0, 1}, {0, 2}, {1, 3}, {1, 4}, {2, 5}, {2, 6}} {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	parent, depth, head, pos := buildHLD(g, 0)
	fmt.Fprintln(out, hldLCA(3, 5, parent, depth, head), hldLCA(4, 6, parent, depth, head))
	printInts(out, head)
	printInts(out, pos)
}
