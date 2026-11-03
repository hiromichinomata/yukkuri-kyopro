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
	cnt := 0
	for i := 0; i < n; i++ {
		var h int
		fmt.Fscan(in, &h)
		if h >= k {
			cnt++
		}
	}
	fmt.Fprintln(out, cnt)
}
