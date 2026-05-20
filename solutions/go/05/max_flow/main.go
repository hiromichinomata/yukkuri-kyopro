package main

import "fmt"

func maxFlow(cap [][]int, s, t, n int) int {
	flow := 0
	for {
		parent := make([]int, n)
		for i := range parent {
			parent[i] = -1
		}
		parent[s] = s
		q := []int{s}
		for head := 0; head < len(q); head++ {
			v := q[head]
			for to := 0; to < n; to++ {
				if parent[to] == -1 && cap[v][to] > 0 {
					parent[to] = v
					q = append(q, to)
				}
			}
		}
		if parent[t] == -1 {
			break
		}
		f := 1 << 60
		v := t
		for v != s {
			if cap[parent[v]][v] < f {
				f = cap[parent[v]][v]
			}
			v = parent[v]
		}
		v = t
		for v != s {
			u := parent[v]
			cap[u][v] -= f
			cap[v][u] += f
			v = u
		}
		flow += f
	}
	return flow
}

func main() {
	n := 4
	cap := make([][]int, n)
	for i := range cap {
		cap[i] = make([]int, n)
	}
	cap[0][1], cap[0][2] = 3, 2
	cap[1][2], cap[1][3] = 1, 2
	cap[2][3] = 3
	fmt.Println(maxFlow(cap, 0, 3, n))
}
