package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// beats は手 x が手 y に勝つか
func beats(x, y byte) bool {
	return (x == 'G' && y == 'C') || (x == 'C' && y == 'P') || (x == 'P' && y == 'G')
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n, &m)
	hands := make([]string, 2*n)
	for i := range hands {
		fmt.Fscan(in, &hands[i])
	}
	wins := make([]int, 2*n)
	rank := make([]int, 2*n) // 順位順の選手番号（0 始まり）
	for i := range rank {
		rank[i] = i
	}
	for j := 0; j < m; j++ {
		for k := 0; k < n; k++ {
			x, y := rank[2*k], rank[2*k+1]
			if beats(hands[x][j], hands[y][j]) {
				wins[x]++
			} else if beats(hands[y][j], hands[x][j]) {
				wins[y]++
			}
		}
		sort.Slice(rank, func(a, b int) bool { // 勝ち数の多い順、同じなら番号の小さい順
			if wins[rank[a]] != wins[rank[b]] {
				return wins[rank[a]] > wins[rank[b]]
			}
			return rank[a] < rank[b]
		})
	}
	for _, i := range rank {
		fmt.Fprintln(out, i+1)
	}
}
