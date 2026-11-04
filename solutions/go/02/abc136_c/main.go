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
	prev := 0 // 直前のマスの（操作後の）高さ
	for i := 0; i < n; i++ {
		var x int
		fmt.Fscan(in, &x)
		if x-1 >= prev { // 下げても大丈夫なら下げる（後ろが楽になる）
			prev = x - 1
		} else if x >= prev { // 下げられないならそのまま
			prev = x
		} else {
			fmt.Fprintln(out, "No")
			return
		}
	}
	fmt.Fprintln(out, "Yes")
}
