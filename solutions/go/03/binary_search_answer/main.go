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
	check := func(x int) bool { return x*x <= n }
	hi := 1
	for check(hi) {
		hi *= 2
	}
	lo, hiAns := 0, hi
	for lo < hiAns {
		mid := (lo + hiAns + 1) / 2
		if check(mid) {
			lo = mid
		} else {
			hiAns = mid - 1
		}
	}
	fmt.Println(lo)
}
