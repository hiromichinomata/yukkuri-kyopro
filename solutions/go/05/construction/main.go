package main

import (
	"bufio"
	"fmt"
	"os"
)

// isValid は隣り合う差の絶対値がすべて異なるかを返す。
func isValid(p []int) bool {
	seen := map[int]bool{}
	for i := 0; i+1 < len(p); i++ {
		d := p[i+1] - p[i]
		if d < 0 {
			d = -d
		}
		if seen[d] {
			return false
		}
		seen[d] = true
	}
	return true
}

// construct は 1, n, 2, n-1, ... と左右から交互に取る。差は n-1, n-2, ..., 1 になる。
func construct(n int) []int {
	res := []int{}
	for lo, hi := 1, n; lo <= hi; lo, hi = lo+1, hi-1 {
		res = append(res, lo)
		if lo != hi {
			res = append(res, hi)
		}
	}
	return res
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	p := construct(n)
	if !isValid(p) {
		panic("construction is wrong")
	}
	for i, x := range p {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, x)
	}
	fmt.Fprintln(out)
}
