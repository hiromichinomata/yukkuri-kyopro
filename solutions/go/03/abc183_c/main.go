package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	t := make([][]int, n)
	for i := range t {
		t[i] = make([]int, n)
		for j := range t[i] {
			fmt.Fscan(in, &t[i][j])
		}
	}
	used := make([]bool, n)
	used[0] = true // 都市 1 は始点・終点に固定
	ans := 0
	var rec func(cur, depth, time int)
	rec = func(cur, depth, time int) {
		if depth == n {
			if time+t[cur][0] == k {
				ans++
			}
			return
		}
		for v := 1; v < n; v++ {
			if !used[v] {
				used[v] = true
				rec(v, depth+1, time+t[cur][v])
				used[v] = false
			}
		}
	}
	rec(0, 1, 0)
	fmt.Println(ans)
}
