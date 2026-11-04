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
	switch {
	case n <= 125:
		fmt.Println(4)
	case n <= 211:
		fmt.Println(6)
	default:
		fmt.Println(8)
	}
}
