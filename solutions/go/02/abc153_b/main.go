package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var h, n int
	fmt.Fscan(in, &h, &n)
	sum := 0
	for i := 0; i < n; i++ {
		var a int
		fmt.Fscan(in, &a)
		sum += a
	}
	// 全部の技を 1 回ずつ使うのが最大のダメージ
	if sum >= h {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
