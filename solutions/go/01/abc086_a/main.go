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

	var a, b int
	fmt.Fscan(in, &a, &b)
	if a*b%2 == 0 { // 2 で割った余りが 0 なら偶数
		fmt.Fprintln(out, "Even")
	} else {
		fmt.Fprintln(out, "Odd")
	}
}
