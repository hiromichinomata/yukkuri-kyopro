package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, x int
	fmt.Fscan(in, &n, &m, &x)
	c := make([]int, n)
	a := make([][]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &c[i])
		a[i] = make([]int, m)
		for j := range a[i] {
			fmt.Fscan(in, &a[i][j])
		}
	}
	const inf = 1 << 60
	best := inf
	for mask := 0; mask < 1<<n; mask++ { // どの本を買うかを 2^N 通り全部試す
		cost := 0
		level := make([]int, m)
		for i := 0; i < n; i++ {
			if mask>>i&1 == 1 {
				cost += c[i]
				for j := 0; j < m; j++ {
					level[j] += a[i][j]
				}
			}
		}
		ok := true
		for _, v := range level {
			if v < x {
				ok = false
			}
		}
		if ok && cost < best {
			best = cost
		}
	}
	if best == inf {
		best = -1
	}
	fmt.Println(best)
}
