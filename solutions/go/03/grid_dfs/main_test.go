package main

import (
	"math/rand"
	"testing"
)

func TestGridDFS(t *testing.T) {
	r := rand.New(rand.NewSource(1))
	for trial := 0; trial < 300; trial++ {
		h, w := r.Intn(5)+1, r.Intn(5)+1
		grid := make([][]byte, h)
		for i := range grid {
			grid[i] = make([]byte, w)
			for j := range grid[i] {
				grid[i][j] = ".#"[r.Intn(3)/2]
			}
		}
		grid[0][0] = '.'
		// BFS で連結成分の大きさを数える
		seenB := map[[2]int]bool{{0, 0}: true}
		q := [][2]int{{0, 0}}
		for k := 0; k < len(q); k++ {
			for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
				ni, nj := q[k][0]+d[0], q[k][1]+d[1]
				p := [2]int{ni, nj}
				if ni >= 0 && ni < h && nj >= 0 && nj < w && grid[ni][nj] == '.' && !seenB[p] {
					seenB[p] = true
					q = append(q, p)
				}
			}
		}
		seen := make([][]bool, h)
		for i := range seen {
			seen[i] = make([]bool, w)
		}
		if got := dfs(0, 0, grid, seen); got != len(q) {
			t.Fatalf("got %d want %d", got, len(q))
		}
	}
}
