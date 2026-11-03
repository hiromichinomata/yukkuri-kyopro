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
	// 区間 (l, r] の和が 0 ⇔ 累積和 S[l] == S[r]
	cnt := map[int]int{0: 1} // S[0] = 0
	s, ans := 0, 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Fscan(in, &x)
		s += x
		ans += cnt[s] // これまでに同じ累積和が出た回数だけ、和 0 の区間が増える
		cnt[s]++
	}
	fmt.Fprintln(out, ans)
}
