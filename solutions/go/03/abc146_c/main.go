package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var a, b, x int64
	fmt.Fscan(in, &a, &b, &x)
	canBuy := func(n int64) bool {
		d := int64(len(strconv.FormatInt(n, 10)))
		return a*n+b*d <= x // a*n ≤ 10^18 なので int64 に収まる
	}
	ok, ng := int64(0), int64(1_000_000_001) // ok: 買える（0 は番兵）, ng: 買えない
	for ng-ok > 1 {
		mid := (ok + ng) / 2
		if canBuy(mid) {
			ok = mid
		} else {
			ng = mid
		}
	}
	fmt.Fprintln(out, ok)
}
