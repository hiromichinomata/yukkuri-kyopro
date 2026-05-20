package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var h, w int
	fmt.Fscan(in, &h, &w)
	grid := make([]string, h)
	si, sj, gi, gj := -1, -1, -1, -1
	for i := 0; i < h; i++ {
		var row string
		fmt.Fscan(in, &row)
		grid[i] = row
		for j := 0; j < w; j++ {
			switch row[j] {
			case 'S':
				si, sj = i, j
			case 'G':
				gi, gj = i, j
			}
		}
	}
	dist := make([][]int, h)
	for i := range dist {
		dist[i] = make([]int, w)
		for j := range dist[i] {
			dist[i][j] = -1
		}
	}
	di := []int{-1, 1, 0, 0}
	dj := []int{0, 0, -1, 1}
	type pos struct{ i, j int }
	q := []pos{{si, sj}}
	dist[si][sj] = 0
	for head := 0; head < len(q); head++ {
		p := q[head]
		for k := 0; k < 4; k++ {
			ni, nj := p.i+di[k], p.j+dj[k]
			if ni < 0 || ni >= h || nj < 0 || nj >= w {
				continue
			}
			if grid[ni][nj] == '#' || dist[ni][nj] != -1 {
				continue
			}
			dist[ni][nj] = dist[p.i][p.j] + 1
			q = append(q, pos{ni, nj})
		}
	}
	fmt.Println(dist[gi][gj])
}
