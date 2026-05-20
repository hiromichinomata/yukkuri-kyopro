package main

import "fmt"

func main() {
	n := 4
	g := [][]int{{1, 2}, {3}, {3}, {}}
	indeg := []int{0, 1, 1, 2}
	q := []int{}
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			q = append(q, i)
		}
	}
	order := []int{}
	for head := 0; head < len(q); head++ {
		v := q[head]
		order = append(order, v)
		for _, to := range g[v] {
			indeg[to]--
			if indeg[to] == 0 {
				q = append(q, to)
			}
		}
	}
	fmt.Println(order)
}
