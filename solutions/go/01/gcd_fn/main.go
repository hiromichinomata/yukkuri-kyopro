package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var a, b int
	fmt.Fscan(in, &a, &b)
	fmt.Println(gcd(a, b))
}
