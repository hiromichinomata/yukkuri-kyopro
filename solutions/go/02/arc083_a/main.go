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

	var a, b, c, d, e, f int
	fmt.Fscan(in, &a, &b, &c, &d, &e, &f)
	// 作れる水の量・砂糖の量を、それぞれ全部列挙する
	waters := map[int]bool{}
	for i := 0; 100*a*i <= f; i++ {
		for j := 0; 100*a*i+100*b*j <= f; j++ {
			if w := 100*a*i + 100*b*j; w > 0 {
				waters[w] = true
			}
		}
	}
	sugars := map[int]bool{}
	for i := 0; c*i <= f; i++ {
		for j := 0; c*i+d*j <= f; j++ {
			sugars[c*i+d*j] = true
		}
	}

	bestTotal, bestSugar := 100*a, 0 // 砂糖なしの水（濃度 0）
	for w := range waters {
		for s := range sugars {
			if w+s > f || s*100 > e*w { // 容量オーバー or 溶け残り
				continue
			}
			// s / (w+s) > bestSugar / bestTotal を、割り算せずに比較
			if s*bestTotal > bestSugar*(w+s) {
				bestTotal, bestSugar = w+s, s
			}
		}
	}
	fmt.Fprintln(out, bestTotal, bestSugar)
}
