package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var a, b, c int
	fmt.Fscan(in, &a, &b, &c)
	ans := a
	if b > ans {
		ans = b
	}
	if c > ans {
		ans = c
	}
	fmt.Println(ans)
}
