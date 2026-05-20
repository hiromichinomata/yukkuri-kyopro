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
	for ; q > 0; q-- {
		var a, b int
		fmt.Fscan(in, &a, &b)
		a--
		b--
		d := a - b
		if d < 0 {
			d = -d
		}
		if d > n-d {
			d = n - d
		}
		fmt.Fprintln(out, d)
	}
}
