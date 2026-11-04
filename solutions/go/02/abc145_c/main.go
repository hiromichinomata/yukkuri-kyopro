package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	x, y := make([]float64, n), make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &x[i], &y[i])
	}
	order := make([]int, n)
	used := make([]bool, n)
	total, count := 0.0, 0
	var rec func(k int) // 順列全探索（N ≤ 8 なので 40320 通り）
	rec = func(k int) {
		if k == n {
			for i := 0; i+1 < n; i++ {
				a, b := order[i], order[i+1]
				total += math.Hypot(x[a]-x[b], y[a]-y[b])
			}
			count++
			return
		}
		for v := 0; v < n; v++ {
			if !used[v] {
				used[v] = true
				order[k] = v
				rec(k + 1)
				used[v] = false
			}
		}
	}
	rec(0)
	fmt.Printf("%.10f\n", total/float64(count))
}
