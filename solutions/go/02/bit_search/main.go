package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, k int
	fmt.Fscan(in, &n, &k)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	count := 0
	for mask := 0; mask < 1<<n; mask++ { // 0 〜 2^n - 1 の全部分集合
		s := 0
		for i := 0; i < n; i++ {
			if mask>>i&1 == 1 { // i ビット目が 1 なら a[i] を選ぶ
				s += a[i]
			}
		}
		if s == k {
			count++
		}
	}
	fmt.Fprintln(out, count)
}
