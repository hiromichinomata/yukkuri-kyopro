package main

import "fmt"

func dfs(i, j int, grid [][]byte, seen [][]bool) int {
	h, w := len(grid), len(grid[0])
	seen[i][j] = true
	size := 1
	di := []int{-1, 1, 0, 0}
	dj := []int{0, 0, -1, 1}
	for k := 0; k < 4; k++ {
		ni, nj := i+di[k], j+dj[k]
		if ni < 0 || ni >= h || nj < 0 || nj >= w {
			continue
		}
		if seen[ni][nj] || grid[ni][nj] != '.' {
			continue
		}
		size += dfs(ni, nj, grid, seen)
	}
	return size
}

func main() {
	grid := [][]byte{
		[]byte("..#."),
		[]byte(".#.."),
		[]byte("...."),
	}
	seen := make([][]bool, 3)
	for i := range seen {
		seen[i] = make([]bool, 4)
	}
	fmt.Println(dfs(0, 0, grid, seen))
}
