package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxV = 50

// reachable[v][w]: v から、allowed の k で余りを取る操作を繰り返して w にできるか
func reachable(allowed []bool) [maxV + 1][maxV + 1]bool {
	var r [maxV + 1][maxV + 1]bool
	for v := 0; v <= maxV; v++ {
		r[v][v] = true
		for k := 1; k <= maxV; k++ {
			if allowed[k] {
				r[v][v%k] = true
			}
		}
	}
	for mid := 0; mid <= maxV; mid++ { // ワーシャルフロイドで推移閉包
		for v := 0; v <= maxV; v++ {
			if r[v][mid] {
				for w := 0; w <= maxV; w++ {
					if r[mid][w] {
						r[v][w] = true
					}
				}
			}
		}
	}
	return r
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	a, b := make([]int, n), make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	for i := range b {
		fmt.Fscan(in, &b[i])
	}
	ok := func(allowed []bool) bool {
		r := reachable(allowed)
		for i := range a {
			if !r[a[i]][b[i]] {
				return false
			}
		}
		return true
	}
	allowed := make([]bool, maxV+1)
	for k := 1; k <= maxV; k++ {
		allowed[k] = true
	}
	if !ok(allowed) {
		fmt.Fprintln(out, -1)
		return
	}
	// 2^k は 2^1 + ... + 2^(k-1) より大きいので、大きい k から「使わずに済むか」を決める
	for k := maxV; k >= 1; k-- {
		allowed[k] = false
		if !ok(allowed) {
			allowed[k] = true
		}
	}
	var ans int64
	for k := 1; k <= maxV; k++ {
		if allowed[k] {
			ans += 1 << k
		}
	}
	fmt.Fprintln(out, ans)
}
