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
	grid := make([]byte, 0, h*w) // 1 次元にして i*w + j で表す
	for i := 0; i < h; i++ {
		var row string
		fmt.Fscan(in, &row)
		grid = append(grid, row...)
	}
	var warp [26][]int // 文字ごとのテレポーター
	s, g := 0, 0
	for idx, ch := range grid {
		switch {
		case 'a' <= ch && ch <= 'z':
			warp[ch-'a'] = append(warp[ch-'a'], idx)
		case ch == 'S':
			s = idx
		case ch == 'G':
			g = idx
		}
	}
	dist := make([]int, h*w)
	for i := range dist {
		dist[i] = -1
	}
	dist[s] = 0
	q := []int{s}
	var used [26]bool
	for head := 0; head < len(q); head++ {
		v := q[head]
		if v == g {
			break
		}
		i, j := v/w, v%w
		nbr := make([]int, 0, 4)
		if i > 0 {
			nbr = append(nbr, v-w)
		}
		if i < h-1 {
			nbr = append(nbr, v+w)
		}
		if j > 0 {
			nbr = append(nbr, v-1)
		}
		if j < w-1 {
			nbr = append(nbr, v+1)
		}
		if ch := grid[v]; 'a' <= ch && ch <= 'z' && !used[ch-'a'] {
			// 同じ文字のテレポートは、最初に使ったときが一番早い → 一度使ったら二度と見ない
			used[ch-'a'] = true
			nbr = append(nbr, warp[ch-'a']...)
		}
		for _, to := range nbr {
			if dist[to] == -1 && grid[to] != '#' {
				dist[to] = dist[v] + 1
				q = append(q, to)
			}
		}
	}
	fmt.Println(dist[g])
}
