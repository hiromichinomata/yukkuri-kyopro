package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	g := make([][]int, n+1)
	for i := 0; i < n-1; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		g[a] = append(g[a], b)
		g[b] = append(g[b], a)
	}
	// 1 を根にする。m[v]: v の親から根までの道の最大 ID
	parent, m := make([]int, n+1), make([]int, n+1)
	parent[1] = -1
	order := []int{1}
	for h := 0; h < len(order); h++ {
		v := order[h]
		for _, c := range g[v] {
			if c != parent[v] {
				parent[c] = v
				m[c] = max(m[v], v)
				order = append(order, c)
			}
		}
	}
	memo := map[[2]int]int{}
	// q(v, x): v の子孫のうち、x 未満の ID だけを通って v から行ける頂点の数（たどった頂点もメモ）
	q := func(v, x int) int {
		if r, ok := memo[[2]int{v, x}]; ok {
			return r
		}
		type item struct {
			u    int
			done bool
		}
		stack := []item{{v, false}}
		for len(stack) > 0 {
			it := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if it.done {
				s := 0
				for _, c := range g[it.u] {
					if c != parent[it.u] && c < x {
						s += 1 + memo[[2]int{c, x}]
					}
				}
				memo[[2]int{it.u, x}] = s
				continue
			}
			stack = append(stack, item{it.u, true})
			for _, c := range g[it.u] {
				if c != parent[it.u] && c < x {
					if _, ok := memo[[2]int{c, x}]; !ok {
						stack = append(stack, item{c, false})
					}
				}
			}
		}
		return memo[[2]int{v, x}]
	}
	c := make([]int, n+1)
	c[1] = 1
	for _, v := range order[1:] {
		p := parent[v]
		if v > m[p] {
			c[v] = c[p] + q(v, m[v]) + 1
		} else {
			c[v] = c[p] + q(v, m[v]) - q(v, m[p])
		}
	}
	for v := 2; v <= n; v++ {
		if v > 2 {
			out.WriteByte(' ')
		}
		out.WriteString(strconv.Itoa(c[v] - 1))
	}
	out.WriteByte('\n')
}
