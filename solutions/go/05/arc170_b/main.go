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
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	// 同じ値が 3 回出ると (x, x, x) が等差。値は 10 種類なので、長さ 21 の区間には
	// どれかの値が 3 回出て、必ず等差の 3 つ組がある（鳩の巣原理）
	const w = 20
	ans := 0
	best := -1 // 右端が k 以下の 3 つ組のうち、左端 i の最大値（なければ -1）
	for k := 0; k < n; k++ {
		lo := k - w - 1
		if lo < -1 {
			lo = -1
		}
		for j := k - 1; j > lo; j-- {
			need := 2*a[j] - a[k] // a[i] - a[j] = a[j] - a[k] を満たす a[i]
			for i := j - 1; i > lo; i-- {
				if a[i] == need {
					if i > best {
						best = i
					}
					break // この j では一番右の i だけ見れば十分
				}
			}
		}
		ans += best + 1 // 右端が k の区間 [l, k] は、l <= best なら良い組
	}
	fmt.Fprintln(out, ans)
}
