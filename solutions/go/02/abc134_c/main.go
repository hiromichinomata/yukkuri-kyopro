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
	fmt.Fscan(in, &n)
	a := make([]int, n)
	iFirst := 0
	for i := range a {
		fmt.Fscan(in, &a[i])
		if a[i] > a[iFirst] {
			iFirst = i
		}
	}
	// 自分以外の最大値は、自分が 1 番大きい値でなければ 1 番大きい値、そうなら 2 番目
	second := 0
	for i, x := range a {
		if i != iFirst && x > second {
			second = x
		}
	}
	for i := range a {
		if i == iFirst {
			fmt.Fprintln(out, second)
		} else {
			fmt.Fprintln(out, a[iFirst])
		}
	}
}
