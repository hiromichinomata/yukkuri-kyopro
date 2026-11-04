package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n, &m)
	odd := 0 // 「1」の個数が奇数の人数
	for i := 0; i < n; i++ {
		var s string
		fmt.Fscan(in, &s)
		if strings.Count(s, "1")%2 == 1 {
			odd++
		}
	}
	even := n - odd
	// 偶奇が違うペアは、どんな正解でも同点にならない
	fmt.Fprintln(out, odd*even)
}
