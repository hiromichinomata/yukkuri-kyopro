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

	var s string
	fmt.Fscan(in, &s)
	best, upper := 0, 0 // upper: i 桁目より上の桁の和
	for _, ch := range s {
		best += int(ch - '0') // N そのもの
	}
	for i := 0; i < len(s); i++ {
		d := int(s[i] - '0')
		if d > 0 {
			// i 桁目を 1 減らし、それより下を全部 9 にした数は N 以下
			if cand := upper + d - 1 + 9*(len(s)-i-1); cand > best {
				best = cand
			}
		}
		upper += d
	}
	fmt.Fprintln(out, best)
}
