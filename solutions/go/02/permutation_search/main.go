package main

import (
	"bufio"
	"fmt"
	"os"
)

// nextPermutation は p を辞書順で次の順列に並べ替える。最後の順列なら false を返す。
func nextPermutation(p []int) bool {
	i := len(p) - 2
	for i >= 0 && p[i] >= p[i+1] {
		i--
	}
	if i < 0 {
		return false
	}
	j := len(p) - 1
	for p[j] <= p[i] {
		j--
	}
	p[i], p[j] = p[j], p[i]
	for l, r := i+1, len(p)-1; l < r; l, r = l+1, r-1 {
		p[l], p[r] = p[r], p[l]
	}
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	d := make([][]int, n)
	for i := range d {
		d[i] = make([]int, n)
		for j := range d[i] {
			fmt.Fscan(in, &d[i][j])
		}
	}
	order := make([]int, 0, n-1)
	for i := 1; i < n; i++ {
		order = append(order, i) // 昇順から始めると全順列を辿れる
	}
	best := 1 << 60
	for {
		cost, cur := 0, 0
		for _, nxt := range order {
			cost += d[cur][nxt]
			cur = nxt
		}
		cost += d[cur][0] // 都市 0 に戻る
		if cost < best {
			best = cost
		}
		if !nextPermutation(order) {
			break
		}
	}
	fmt.Fprintln(out, best)
}
