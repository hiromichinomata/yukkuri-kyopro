package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	sort.Ints(a) // ソートすると |a_i - a_j| = a_j - a_i（i < j）
	ans, prefix := 0, 0
	for j, x := range a {
		// a_j は「自分より前の j 個」との差で j 回足され、前の値の和が引かれる（主客転倒）
		ans += x*j - prefix
		prefix += x
	}
	fmt.Println(ans)
}
