package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	kinds := map[int]bool{}
	for i := 0; i < n; i++ {
		var d int
		fmt.Fscan(in, &d)
		kinds[d] = true
	}
	// 直径が真に小さいものしか上に積めない → 使えるのは「異なる直径」の種類数だけ
	fmt.Println(len(kinds))
}
