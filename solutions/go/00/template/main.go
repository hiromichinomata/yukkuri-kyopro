package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	inf int64 = 1 << 60
	mod int   = 998244353
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	// 例: var n int
	// fmt.Fscan(in, &n)
	// 例: xs := make([]int, n); for i := range xs { fmt.Fscan(in, &xs[i]) }
	_ = in
}
