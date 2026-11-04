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

	var n int
	fmt.Fscan(in, &n)
	prefix := 0         // A_1 + ... + A_k
	prefixOfPrefix := 0 // (A_1) + (A_1 + A_2) + ... + (A_1 + ... + A_k)
	mx := 0             // max(A_1, ..., A_k)
	for k := 1; k <= n; k++ {
		var x int
		fmt.Fscan(in, &x)
		prefix += x
		prefixOfPrefix += prefix
		if x > mx {
			mx = x
		}
		// 操作後の和 = 累積和の累積和 + k × 最大値
		fmt.Fprintln(out, prefixOfPrefix+k*mx)
	}
}
