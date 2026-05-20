package main

import "fmt"

func main() {
	n := 5
	g := make([][]int, n)
	edges := [][2]int{{0, 1}, {0, 2}, {1, 3}, {2, 4}}
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	fmt.Println(g)
}
