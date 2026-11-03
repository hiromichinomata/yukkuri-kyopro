package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	total := 0.0
	for start := 1; start <= n; start++ { // サイコロの目ごとに勝つ確率を足す
		score, p := start, 1.0
		for score < k { // K 以上になるまで表を出し続ける必要がある
			score *= 2
			p /= 2
		}
		total += p
	}
	fmt.Printf("%.12f\n", total/float64(n))
}
