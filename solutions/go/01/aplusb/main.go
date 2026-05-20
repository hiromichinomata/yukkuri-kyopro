package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var a, b int
	if _, err := fmt.Fscan(in, &a, &b); err != nil {
		panic(err)
	}
	fmt.Println(a + b)
}
