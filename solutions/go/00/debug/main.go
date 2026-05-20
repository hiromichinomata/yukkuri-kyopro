package main

import (
	"fmt"
	"os"
)

func debug(args ...any) {
	fmt.Fprintln(os.Stderr, args...)
}

func main() {
	debug("local only", true)
}
