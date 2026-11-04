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

	var n, q int
	fmt.Fscan(in, &n, &q)
	diff := make([]int, n+1) // いもす法: 区間 [l, r] に +1 → diff[l-1]++, diff[r]--
	for ; q > 0; q-- {
		var l, r int
		fmt.Fscan(in, &l, &r)
		diff[l-1]++
		diff[r]--
	}
	b := make([]byte, n)
	cnt := 0
	for i := 0; i < n; i++ {
		cnt += diff[i]           // 駒 i が裏返された回数
		b[i] = byte('0' + cnt%2) // 奇数回なら白（1）
	}
	fmt.Fprintln(out, string(b))
}
