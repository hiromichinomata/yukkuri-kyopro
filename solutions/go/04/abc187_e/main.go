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

	var n int
	fmt.Fscan(in, &n)
	ea, eb := make([]int, n-1), make([]int, n-1)
	g := make([][]int, n)
	for i := 0; i < n-1; i++ {
		fmt.Fscan(in, &ea[i], &eb[i])
		ea[i]--
		eb[i]--
		g[ea[i]] = append(g[ea[i]], eb[i])
		g[eb[i]] = append(g[eb[i]], ea[i])
	}
	// 頂点 0 を根にして親と訪問順を求める
	parent := make([]int, n)
	parent[0] = -1
	seen := make([]bool, n)
	seen[0] = true
	order := []int{0}
	for head := 0; head < len(order); head++ {
		v := order[head]
		for _, to := range g[v] {
			if !seen[to] {
				seen[to] = true
				parent[to] = v
				order = append(order, to)
			}
		}
	}
	add := make([]int, n) // add[v]: v の部分木全体に足す値（最後に根から累積する）
	var q int
	fmt.Fscan(in, &q)
	for ; q > 0; q-- {
		var t, e, x int
		fmt.Fscan(in, &t, &e, &x)
		a, b := ea[e-1], eb[e-1]
		if t == 2 {
			a, b = b, a // 「b を通らずに a から行ける頂点」に足す、に統一
		}
		if parent[a] == b {
			add[a] += x // a が子 → a の部分木だけ
		} else {
			add[0] += x // a が親 → 全体に足して b の部分木から引く
			add[b] -= x
		}
	}
	for _, v := range order[1:] { // 根から順に、親の値を子へ足し込む（木の上の累積和）
		add[v] += add[parent[v]]
	}
	for _, v := range add {
		fmt.Fprintln(out, v)
	}
}
