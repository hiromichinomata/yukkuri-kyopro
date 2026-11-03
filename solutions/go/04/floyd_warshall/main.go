package main

import (
	"fmt"
	"strings"
)

func main() {
	const INF = 1 << 60
	dist := [][]int{
		{0, 3, INF},
		{INF, 0, 1},
		{2, INF, 0},
	}
	n := len(dist)
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if dist[i][k] >= INF || dist[k][j] >= INF {
					continue
				}
				if dist[i][j] > dist[i][k]+dist[k][j] {
					dist[i][j] = dist[i][k] + dist[k][j]
				}
			}
		}
	}
	for _, row := range dist {
		fmt.Println(strings.Trim(fmt.Sprint(row), "[]"))
	}
}
