package main

import (
	"bufio"
	"fmt"
	"os"
)

// AGC004 A - Divide a Cuboid
// どれかの辺が偶数なら 0。全部奇数なら、残り 2 辺の積の最小値が答え。
func main() {
	in := bufio.NewReader(os.Stdin)
	var a, b, c int
	fmt.Fscan(in, &a, &b, &c)
	if a%2 == 0 || b%2 == 0 || c%2 == 0 {
		fmt.Println(0)
		return
	}
	fmt.Println(min(a*b, b*c, c*a))
}
