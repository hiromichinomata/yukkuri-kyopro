package main

import (
	"fmt"
	"os"
)

func debug(args ...any) {
	fmt.Fprintln(os.Stderr, args...)
}

func main() {
	debug("local only", 42) // 標準エラー出力なので、提出しても判定には影響しない
}
