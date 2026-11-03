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

	var n int
	var s string
	fmt.Fscan(in, &n, &s)
	b := []byte(s)
	for i, ch := range b {
		c := (int(ch-'A') + n) % 26 // Z の次は A
		b[i] = byte('A' + c)
	}
	fmt.Fprintln(out, string(b))
}
