package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	solved := make([]bool, n+1)
	wa := make([]int, n+1) // 最初の AC までの WA の数
	for i := 0; i < m; i++ {
		var p int
		var s string
		fmt.Fscan(in, &p, &s)
		if solved[p] {
			continue // AC 後の提出は数えない
		}
		if s == "AC" {
			solved[p] = true
		} else {
			wa[p]++
		}
	}
	ac, penalty := 0, 0
	for p := 1; p <= n; p++ {
		if solved[p] {
			ac++
			penalty += wa[p] // AC した問題の WA だけ
		}
	}
	fmt.Println(ac, penalty)
}
