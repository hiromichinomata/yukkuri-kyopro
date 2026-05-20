package main

import "fmt"

func main() {
	grid := [][]byte{
		[]byte("..#."),
		[]byte(".#.."),
		[]byte("...."),
	}
	h, w := len(grid), len(grid[0])
	di := []int{-1, 1, 0, 0}
	dj := []int{0, 0, -1, 1}
	si, sj := 1, 0
	var ok [][2]int
	for k := 0; k < 4; k++ {
		ni, nj := si+di[k], sj+dj[k]
		if 0 <= ni && ni < h && 0 <= nj && nj < w && grid[ni][nj] != '#' {
			ok = append(ok, [2]int{ni, nj})
		}
	}
	fmt.Println(ok)
}
