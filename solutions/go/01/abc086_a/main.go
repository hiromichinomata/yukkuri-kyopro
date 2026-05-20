package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var a, b int
	fmt.Fscan(in, &a, &b)
	p := a * b
	if 1 <= p && p <= 9 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
