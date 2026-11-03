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
	// 連結成分に k 頂点入っているとき、外の頂点を選ぶ確率は (n-k)/n。
	// 成功確率 p の試行を成功まで繰り返す回数の期待値は 1/p なので、
	// k = 1, ..., n-1 の n/(n-k) を足す（期待値の線形性）
	ans := 0.0
	for k := 1; k < n; k++ {
		ans += float64(n) / float64(n-k)
	}
	fmt.Printf("%.10f\n", ans)
}
