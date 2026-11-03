package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var s string
	fmt.Fscan(in, &s)        // 空白を含まないので 1 語として読める
	if s == "Hello,World!" { // 大文字・記号まで完全一致
		fmt.Println("AC")
	} else {
		fmt.Println("WA")
	}
}
