package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var s string
	var k int
	fmt.Fscan(in, &s, &k)
	ans, left, dots := 0, 0, 0
	for right := 0; right < len(s); right++ { // 尺取り法: 区間 [left, right] の「.」を K 個以下に保つ
		if s[right] == '.' {
			dots++
		}
		for dots > k {
			if s[left] == '.' {
				dots--
			}
			left++
		}
		if right-left+1 > ans {
			ans = right - left + 1
		}
	}
	fmt.Println(ans)
}
