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
	// 主客転倒: K × f(K) の和 = 「d が約数になる K」すべてについての K の和を、d ごとに足したもの。
	// d の倍数 d, 2d, …, md（m = N / d）の和は d × m(m+1)/2
	ans := 0
	for d := 1; d <= n; d++ {
		m := n / d
		ans += d * m * (m + 1) / 2
	}
	fmt.Println(ans)
}
