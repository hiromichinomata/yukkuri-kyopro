package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var s string
	fmt.Fscan(in, &s)
	if len(s) < 26 {
		// まだ使っていない文字があれば、一番小さいものを末尾に足すのが次の単語
		used := [26]bool{}
		for _, ch := range s {
			used[ch-'a'] = true
		}
		for c := 0; c < 26; c++ {
			if !used[c] {
				fmt.Println(s + string(rune('a'+c)))
				return
			}
		}
	}
	// 26 文字全部使っているとき: 後ろから見て、s[i] をそれより後ろにある大きい文字に替えられる
	// 一番後ろの位置 i を探し、s[:i] + （s[i] より大きい文字のうち最小）
	for i := 25; i >= 0; i-- {
		best := byte(0)
		for j := i + 1; j < 26; j++ {
			if s[j] > s[i] && (best == 0 || s[j] < best) {
				best = s[j]
			}
		}
		if best != 0 {
			fmt.Println(s[:i] + string(best))
			return
		}
	}
	fmt.Println(-1) // "zyx…a" は最後の単語
}
