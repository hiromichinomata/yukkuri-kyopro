package main

import (
	"bufio"
	"fmt"
	"os"
)

func shift(ch byte, x int) byte {
	if ch < 'A' || ch > 'Z' {
		return ch
	}
	c := int(ch-'A') + x
	c %= 26
	return byte('A' + c)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, x int
	fmt.Fscan(in, &n)
	var s string
	fmt.Fscan(in, &s)
	fmt.Fscan(in, &x)
	out := make([]byte, n)
	for i := 0; i < n; i++ {
		out[i] = shift(s[i], x)
	}
	fmt.Println(string(out))
}
