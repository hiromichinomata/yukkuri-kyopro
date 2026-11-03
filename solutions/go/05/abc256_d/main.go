package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)
	iv := make([][2]int, n)
	for i := range iv {
		fmt.Fscan(in, &iv[i][0], &iv[i][1])
	}
	sort.Slice(iv, func(i, j int) bool { return iv[i][0] < iv[j][0] }) // 左端の順に並べる
	curL, curR := iv[0][0], iv[0][1]
	for _, p := range iv[1:] {
		if p[0] <= curR { // 重なる・接する（半開区間 [l, r) なので l == curR もつながる）
			if p[1] > curR {
				curR = p[1]
			}
		} else {
			fmt.Fprintln(out, curL, curR)
			curL, curR = p[0], p[1]
		}
	}
	fmt.Fprintln(out, curL, curR)
}
