package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var t, n int
	fmt.Fscan(in, &t, &n)
	// 税抜き A が 100 増えると、税込みはちょうど 100 + t 増える（周期性）。
	// 1 周期（A = 1〜100）の税込み価格を並べると、1〜(100+t) のうち t 個が抜ける
	price := map[int]bool{}
	for a := 1; a <= 100; a++ {
		price[(100+t)*a/100] = true
	}
	missing := []int{}
	for v := 1; v <= 100+t; v++ {
		if !price[v] {
			missing = append(missing, v)
		}
	}
	q, r := (n-1)/t, (n-1)%t // 何周目の何番目か
	fmt.Println(q*(100+t) + missing[r])
}
