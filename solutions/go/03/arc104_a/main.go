package main

import (
	"bufio"
	"fmt"
	"os"
)

// ARC104 A - Plus Minus
// X + Y = A、X - Y = B なので X = (A+B)/2、Y = (A-B)/2。
func main() {
	in := bufio.NewReader(os.Stdin)
	var a, b int
	fmt.Fscan(in, &a, &b)
	fmt.Println((a+b)/2, (a-b)/2)
}
