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
	xs := make([]int, n)
	for i := range xs {
		fmt.Fscan(in, &xs[i])
	}
	score := [2]int{} // score[0]: 先手, score[1]: 後手
	turn := 0
	for i := 0; i < n; i++ { // 左端から 1 枚ずつ取る
		score[turn] += xs[i]
		turn ^= 1 // 手番の交代は 1 か所で
	}
	fmt.Fprintln(out, score[0]-score[1])
}
