package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// base は 2K ≤ length ≤ 4K のときの辞書順最小（値は 1 始まり）
func base(length, k int) []int {
	a := make([]int, length)
	for i := 1; i <= length; i++ {
		var v int
		if length <= 3*k {
			if i <= length-k {
				v = i + k
			} else {
				v = i - length + k
			}
		} else {
			switch {
			case i <= k:
				v = i + k
			case i <= length-2*k:
				v = i - k
			case i <= length-k:
				v = i + k
			case i <= 3*k:
				v = i - 2*k
			default:
				v = i - k
			}
		}
		a[i-1] = v
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, k int
	fmt.Fscan(in, &n, &k)
	if n < 2*k {
		fmt.Fprintln(out, -1)
		return
	}
	ans := make([]int, 0, n)
	offset := 0
	// 残りが 4K を超える間は、先頭 2K 個を (K+1, …, 2K, 1, …, K) で埋める
	for n-offset > 4*k {
		for v := k + 1; v <= 2*k; v++ {
			ans = append(ans, offset+v)
		}
		for v := 1; v <= k; v++ {
			ans = append(ans, offset+v)
		}
		offset += 2 * k
	}
	for _, v := range base(n-offset, k) {
		ans = append(ans, offset+v)
	}
	fmt.Fprintln(out, strings.Trim(fmt.Sprint(ans), "[]"))
}
