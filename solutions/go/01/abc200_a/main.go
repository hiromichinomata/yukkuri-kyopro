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
	fmt.Println((n + 99) / 100) // 100 で割って切り上げ（1〜100 年が 1 世紀）
}
