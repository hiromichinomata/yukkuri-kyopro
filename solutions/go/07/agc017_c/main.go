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

	var n, m int
	fmt.Fscan(in, &n, &m)
	a := make([]int, n)
	// 値 v のボールが c 個あると区間 (v-c, v] を覆う。答えは覆われていない位置 1〜N の数
	cnt := make([]int, n+1)
	cover := make([]int, n+1)
	for i := range a {
		fmt.Fscan(in, &a[i])
		cnt[a[i]]++
		if p := a[i] - cnt[a[i]] + 1; p >= 1 { // 値 v の k 個目のボールは位置 v-k+1 を覆う
			cover[p]++
		}
	}
	zeros := 0
	for p := 1; p <= n; p++ {
		if cover[p] == 0 {
			zeros++
		}
	}
	change := func(p, d int) {
		if p < 1 {
			return
		}
		if cover[p] == 0 {
			zeros--
		}
		cover[p] += d
		if cover[p] == 0 {
			zeros++
		}
	}
	for ; m > 0; m-- {
		var x, y int
		fmt.Fscan(in, &x, &y)
		old := a[x-1]
		change(old-cnt[old]+1, -1) // 値 old の最後のボールが覆っていた位置
		cnt[old]--
		cnt[y]++
		change(y-cnt[y]+1, 1)
		a[x-1] = y
		fmt.Fprintln(out, zeros)
	}
}
