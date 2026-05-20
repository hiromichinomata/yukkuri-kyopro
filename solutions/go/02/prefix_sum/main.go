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

	var n, q int
	fmt.Fscan(in, &n, &q)
	a := make([]int, n+1)
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &a[i])
	}
	cum := make([]int, n+1)
	for i := 1; i <= n; i++ {
		cum[i] = cum[i-1] + a[i]
	}
	for ; q > 0; q-- {
		var l, r int
		fmt.Fscan(in, &l, &r)
		fmt.Fprintln(out, cum[r]-cum[l-1])
	}
}
