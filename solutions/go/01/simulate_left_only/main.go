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
	xs := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &xs[i])
	}
	t := 0
	for len(xs) > 0 {
		t += xs[0]
		xs = xs[1:]
	}
	fmt.Println(t)
}
